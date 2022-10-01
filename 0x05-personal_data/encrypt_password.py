#!/usr/bin/env python3
"""Implement a main function that takes no arguments and returns nothing."""
import bcrypt


def hash_password(password: str) -> bytes:
    """functiooon password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """functiooon valid"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
