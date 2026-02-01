{
    'targets': [
     {
        'target_name': 'hello',
        'sources': [
            'node_hello.cc'
        ],
        'conditions': [
            ['OS == "win"',
            {
                'libraries': ['-lnode.lib']
            }
            ]
        ]
    }
    ]
}

