//     Dev: wh0ami
// License: Public Domain <https://unlicense.org>
// Project: https://codeberg.org/wh0ami/prometheus-alertmanager-rocket-chat

class Script {
    process_incoming_request({
                                 request
                             }) {

        // log the incoming data from alertmanager for debugging (can be seen in Rocket.Chat logs)
        console.log(request.content);

        // initialize empty variables
        let attachments = [];
        let attachment = null;
        let fields = null;
        let emoji = null;

        // iterate over all alerts
        if (request.content.alerts) {
        request.content.alerts.forEach(alert => {
            // initialize attachment array
            attachment = {
                "title": alert.labels.alertname + " on instance " + alert.labels.instance,
                "title_link": alert.generatorURL
            };

            // determine alert color
            switch (alert.status) {
                case "resolved":
                    attachment.color = "good";
                    emoji = ":white_check_mark:";
                    break;
                case "firing":
                    attachment.color = "danger";
                    emoji = ":warning:";
                    break;
                default:
                    attachment.color = "warning";
                    emoji = ":warning:";
            }

            // initialize empty list for fields
            fields = [];

            // add the status of the alert to the fields
            fields.push({
                title: "Status", value: emoji + " " + alert.status, short: true
            });

            // add the severity of the alert to the fields, if its defined
            if (!!alert.status) {
                fields.push({
                    title: "Severity", value: alert.labels.severity, short: true
                });
            }

            // add the start time of the alert to the fields
            fields.push({
                title: "Start time", value: alert.startsAt, short: true
            });

            // if the status is resolved, then we will add the end time to the fields
            if (alert.status === "resolved") {
                fields.push({
                    title: "End time", value: alert.endsAt, short: true
                });
            } else {
                // if the status is not resolved, add fields with more detailed information

                // add the summary of the alert to the fields, if its defined
                if (!!alert.annotations.summary) {
                    fields.push({
                        title: "Summary", value: alert.annotations.summary, short: false
                    });
                }

                // add the description of the alert to the fields, if its defined
                if (!!alert.annotations.description) {
                    fields.push({
                        title: "Description", value: alert.annotations.description, short: false
                    });
                }
            }

            // add the fields to the attachment
            attachment.fields = fields;

            // add the attachment to the list of attachments
            attachments.push(attachment);
        });
    }

        return {
            content: {
                username: "Prometheus Monitoring", attachments: attachments
            }
        };

        return {
            error: {
                success: false
            }
        };
    }
}
