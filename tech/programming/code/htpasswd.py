#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple htpasswd-like user manager that works on Windows and Unix.

🔧 Purpose:
    Manage a text-based user/password file (one user per line: username:hash).
    Supports adding, updating, and deleting users. Compatible with Windows.

⚠️ Security Notice:
    This script uses a custom SHA-256-based password hash with salt for basic
    security, but it is **not compatible with Apache htpasswd** formats like $6$.
    It is suitable for internal tools, learning, or low-security use cases only.
    For real-world applications, use a proper password hash like bcrypt or Argon2,
    ideally via libraries like passlib (not used here to meet "no third-party" goal).

📝 File Format:
    Each line is: username:hash
    Example:
        alice:5e884898da28... (SHA-256 hash of 'password' + salt)

🔧 Features:
    - Add/update a user with a password
    - Delete a user
    - Create the file if it does not exist (with -c/--create)
    - Works on Windows and Unix
    - No third-party libraries used (only Python standard library)

📜 Usage:
    python htpasswd_compat.py <filename> <username> [password] [options]

    Where:
        <filename>   : Path to the user/password text file (e.g. users.txt)
        <username>   : The username to add/update/delete
        [password]   : The password (REQUIRED for add/update, OMIT for delete)

    Options:
        -c, --create : Create the file if it does not exist
        -D, --delete : Delete the specified user (no password needed)

🔐 Examples:
    1. Add/update a user (creates file with -c):
        python htpasswd_compat.py users.txt alice mypassword -c

    2. Update a user's password:
        python htpasswd_compat.py users.txt alice newpassword

    3. Delete a user:
        python htpasswd_compat.py users.txt alice -D
"""

import os
import sys
import argparse
import hashlib
import secrets
from pathlib import Path


def generate_salt(length: int = 8) -> str:
    """Generate a random salt string using ASCII letters and digits."""
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(secrets.choice(chars) for _ in range(length))


def hash_password(password: str, salt: str) -> str:
    """Create a simple SHA-256 hash of password + salt."""
    combined = password + salt
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()


class UserPasswdFile:
    def __init__(self, filepath: str, create: bool = False):
        self.filepath = Path(filepath)
        self.entries = []  # List of [username, hash]
        if not create:
            if not self.filepath.exists():
                raise FileNotFoundError(f"File '{filepath}' does not exist.")
            self.load()

    def load(self) -> None:
        """Load user:hash entries from the file."""
        with self.filepath.open('r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(':', 1)
                if len(parts) == 2:
                    self.entries.append([parts[0], parts[1]])

    def save(self) -> None:
        """Save the current user:hash list to the file."""
        with self.filepath.open('w', encoding='utf-8') as f:
            for username, pwhash in self.entries:
                f.write(f"{username}:{pwhash}\n")

    def update(self, username: str, password: str) -> None:
        """Add or update a user with hashed password."""
        salt = generate_salt()
        pwhash = hash_password(password, salt)
        for entry in self.entries:
            if entry[0] == username:
                entry[1] = pwhash
                return
        self.entries.append([username, pwhash])

    def delete(self, username: str) -> None:
        """Delete a user by username."""
        self.entries = [entry for entry in self.entries if entry[0] != username]


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple htpasswd-compatible user manager (Windows-friendly).")
    parser.add_argument('filename', help="Path to the user/password file")
    parser.add_argument('username', help="Username to add/update/delete")
    parser.add_argument('password', nargs='?', default=None, help="Password (required to add/update)")
    parser.add_argument('-c', '--create', action='store_true', help='Create file if it does not exist')
    parser.add_argument('-D', '--delete', action='store_true', help='Delete the user (no password needed)')

    args = parser.parse_args()

    try:
        if args.delete:
            if args.password is not None:
                sys.stderr.write("Error: Do not provide a password when deleting a user.\n")
                sys.exit(1)

            db = UserPasswdFile(args.filename, create=args.create)
            db.delete(args.username)
            db.save()
            print(f"[+] Deleted user: {args.username}")

        else:
            if args.password is None:
                sys.stderr.write("Error: Password is required to add or update a user.\n")
                sys.exit(1)

            db = UserPasswdFile(args.filename, create=args.create)
            db.update(args.username, args.password)
            db.save()
            print(f"[+] Added/Updated user: {args.username}")

    except FileNotFoundError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()