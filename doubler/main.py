# SPDX-FileCopyrightText: 2025 Kaito Kubota
# SPDX-License-Identifier: BSD-3-Clause

import sys

def main():
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                val = float(line)
                ans = val ** 2
                print(ans)
            except ValueError:
                pass
    except BrokenPipeError:
        sys.exit(1)

if __name__ == '__main__':
    main()
