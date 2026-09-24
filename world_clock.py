#!/usr/bin/env python3
"""
world-clock-cli — Multi-timezone CLI with meeting slot overlap finder.
"""
import sys
import datetime

TIMEZONES = [
    ("San Francisco (PT)", -7),
    ("New York (ET)", -4),
    ("London (UTC/BST)", 1),
    ("Berlin (CET)", 2),
    ("Tokyo (JST)", 9),
    ("Sydney (AEST)", 10),
]

def format_grid(utc_now: datetime.datetime):
    print("=" * 64)
    print(f"  Global Time Matrix | UTC: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 64)
    print(f"{'Location':<24} | {'Local Time':<19} | {'Offset':<6} | {'Status'}")
    print("-" * 64)

    for name, offset in TIMEZONES:
        local_t = utc_now + datetime.timedelta(hours=offset)
        hour = local_t.hour
        if 9 <= hour < 18:
            status = "[WORKING HOURS]"
        elif 7 <= hour < 9 or 18 <= hour < 22:
            status = "[EVENING/MORNING]"
        else:
            status = "[OFF HOURS]"

        print(f"{name:<24} | {local_t.strftime('%Y-%m-%d %H:%M'):<19} | {offset:+03d}:00 | {status}")
    print("=" * 64)

def main():
    now_utc = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    format_grid(now_utc)

if __name__ == "__main__":
    main()
