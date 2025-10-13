#!/usr/bin/env python3
"""
Simple, robust Codebreaker (3-digit) game

Instructions:
- You must guess the 3-digit secret code. Digits may repeat.
- You have 6 attempts to guess the correct code.
- After each guess, you'll receive feedback using emojis:
  ✅ means the digit is correct and in the right position.
  ⚠️ means the digit is in the code but in the wrong position.
  ❌ means the digit is not in the code at all.
- Example: For secret 123 and guess 321 → ⚠️3 ⚠️2 ⚠️1

Run:
  python3 codebreaker_hacker_mode.py        # interactive if run in a terminal
  python3 codebreaker_hacker_mode.py --auto  # runs in non-interactive/sandboxed env
  python3 codebreaker_hacker_mode.py --test  # run tests

Environment variable for simulated inputs (comma separated):
  CODEBREAKER_INPUTS="000,111,222"
"""

from __future__ import annotations

import argparse
import os
import random
import sys
from typing import List, Optional

_input_manager: Optional['InputManager'] = None


class InputManager:
    def __init__(self, simulated: Optional[List[str]] = None, default: str = 'quit'):
        self.simulated = list(simulated) if simulated else []
        self.default = default
        try:
            self.interactive = sys.stdin.isatty() and sys.stdout.isatty()
        except Exception:
            self.interactive = False

    def get(self, prompt: str = '') -> str:
        try:
            if self.interactive:
                return input(prompt + ' ').strip()
            if self.simulated:
                resp = self.simulated.pop(0)
                print(f"{prompt} {resp}")
                return resp
            print(f"{prompt} {self.default}  # default (non-interactive)")
            return self.default
        except (EOFError, OSError):
            if self.simulated:
                resp = self.simulated.pop(0)
                print(f"{prompt} {resp}  # fallback after input error")
                return resp
            print(f"{prompt} {self.default}  # fallback after input error")
            return self.default


def safe_input(prompt: str = '') -> str:
    global _input_manager
    if _input_manager is None:
        _input_manager = InputManager(simulated=None, default='quit')
    return _input_manager.get(prompt)


def generate_code(length: int = 3) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def give_feedback(secret: str, guess: str) -> str:
    secret_list = list(secret)
    feedback_tokens: List[str] = [''] * len(guess)

    for i, g in enumerate(guess):
        if i < len(secret) and g == secret[i]:
            feedback_tokens[i] = '✅'
            secret_list[i] = None

    for i, g in enumerate(guess):
        if feedback_tokens[i]:
            continue
        if g in secret_list:
            feedback_tokens[i] = '⚠️'
            secret_list[secret_list.index(g)] = None
        else:
            feedback_tokens[i] = '❌'

    pairs = []
    for i, tok in enumerate(feedback_tokens):
        ch = guess[i] if i < len(guess) else '?'
        pairs.append(f"{tok}{ch}")
    return ' '.join(pairs)


def play_simple() -> None:
    print("=== CODEBREAKER: SIMPLE EDITION1 ===")
    print("Instructions:")
    print("✅ means the digit is correct and in the right place.")
    print("⚠️ means the digit is in the code but in the wrong place.")
    print("❌ means the digit is not in the code at all.")
    print("You have 6 attempts to guess the 3-digit secret code. Digits may repeat.\n")

    secret = generate_code(3)
    attempts = 6

    while attempts > 0:
        prompt = f"[{attempts} attempts left] Enter guess (3 digits):"
        guess = safe_input(prompt).strip()

        if guess.lower() in ('quit', 'exit', 'giveup'):
            print("Quitting game.")
            return

        if len(guess) != 3 or not guess.isdigit():
            print("Enter exactly 3 digits (e.g. 042).")
            continue

        if guess == secret:
            print("ACCESS GRANTED! ✅ You win!")
            return

        print(give_feedback(secret, guess))
        attempts -= 1

    print(f"ACCESS DENIED. The code was {secret}.")


def run_tests() -> bool:
    errors: List[str] = []

    def assert_eq(a, b, msg=''):
        if a != b:
            errors.append(f"Assertion failed: {a!r} != {b!r}. {msg}")

    for ln in (1, 3, 5):
        c = generate_code(ln)
        assert_eq(len(c), ln)
        assert_eq(c.isdigit(), True)

    assert_eq(give_feedback('123', '123'), '✅1 ✅2 ✅3')
    assert_eq(give_feedback('1234', '4123'), '⚠️4 ⚠️1 ⚠️2 ⚠️3')
    assert_eq(give_feedback('1234', '5678'), '❌5 ❌6 ❌7 ❌8')
    expected = '⚠️2 ⚠️1 ✅2 ❌2'
    assert_eq(give_feedback('1223', '2122'), expected)

    global _input_manager
    saved = _input_manager
    try:
        _input_manager = InputManager(simulated=['quit'], default='quit')
        r = safe_input('> ')
        assert_eq(r, 'quit')
    finally:
        _input_manager = saved

    if errors:
        print('\nTESTS FAILED:')
        for e in errors:
            print(' -', e)
        return False
    print('\nAll tests passed.')
    return True


def parse_args():
    p = argparse.ArgumentParser(description='Simple Codebreaker (robust)')
    p.add_argument('--test', action='store_true', help='Run tests and exit')
    p.add_argument('--auto', action='store_true', help='Run in auto/demo mode (non-interactive)')
    p.add_argument('--sim', type=str, help='Simulated inputs (comma-separated)')
    return p.parse_args()


def build_input_manager(args) -> InputManager:
    sim_list: Optional[List[str]] = None
    if args.sim:
        sim_list = [s.strip() for s in args.sim.split(',') if s.strip()]
    else:
        env = os.environ.get('CODEBREAKER_INPUTS')
        if env:
            sim_list = [s.strip() for s in env.split(',') if s.strip()]

    if args.auto and not sim_list:
        sim_list = [f"{d}{d}{d}" for d in '012345']

    return InputManager(simulated=sim_list, default='quit')


def main() -> int:
    global _input_manager
    args = parse_args()
    _input_manager = build_input_manager(args)

    if args.test:
        ok = run_tests()
        return 0 if ok else 2

    if not _input_manager.interactive and not _input_manager.simulated:
        print('Notice: Non-interactive environment detected and no simulated inputs provided.')
        print('Running tests (use --auto to run a demo instead)')
        run_tests()
        print('\nTo play the game interactively, run this script in a terminal.')
        print("To run a non-interactive demo: python3 codebreaker_hacker_mode.py --auto")
        return 0

    try:
        play_simple()
    except Exception as e:
        print('An unexpected error occurred during play:', e)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())