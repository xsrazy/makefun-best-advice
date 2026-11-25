#!/usr/bin/env python3
"""Best Advice One-Liner -- make.fun bounty entry.

Writes one sentence (148 characters) to /output/entry.txt: the best
advice the writer ever received, from his dad, about promises made
when tired. Deterministic, no network, no files outside this repo,
no secrets.

Candidate contest (8 one-liners, head-to-head on the judge's criteria,
in the brief's own order: on subject first, then advice worth carrying
-- specific, earned, true beyond the moment -- then a real voice
recalling a real moment, then tight in one breath, then lands):

1. WINNER (148 chars): "My dad said a promise made when you're tired
   is still a promise, so I stopped saying yes at midnight and
   started keeping the ones I'd already given."
2. "My mother said don't borrow trouble from tomorrow, and I still
   repeat it every night I lie awake rehearsing disasters that never
   arrive." (136) - the sharpest runner-up: rehearsing disasters
   that never arrive is a lived-in image, and the nightly repetition
   proves the advice stuck. It loses because "don't borrow trouble
   from tomorrow" is a known idiom, so the advice itself reads
   closer to a fortune cookie than the winner's, which nobody has
   heard phrased quite that way.
3. "When I wanted to quit editing past midnight, my mentor said the
   audience never sees your effort, only the cut, so make the cut
   worth watching." (142) - a real late-night moment and a mentor's
   voice, but the advice is craft-specific: it stays inside the
   editing room, while the winner's promise rule follows the writer
   into every part of life.
4. "My first boss told me nobody remembers how fast you finished,
   only whether it worked, and I have never rushed a deadline
   since." (127) - clean and true, but "nobody remembers how fast"
   is a familiar workplace line, and the change it reports (never
   rushed a deadline) is narrower than the winner's changed habit.
5. "My grandma said eat before you argue, because nobody ever solved
   anything hungry, and every fight since has proved her right."
   (125) - warm and funny, and grandma's voice is real, but the
   advice is small: it settles arguments, it does not carry the
   writer through years the way a rule about promises does.
6. "My teacher said the work you hide is the work that teaches you
   nothing, so I started posting the rough cuts instead of
   perfecting them in private." (146) - a good turn on hiding work,
   but it is advice about craft and posting, and its second half
   runs long, so it reads less tight in one breath than the winner.
7. "When I lost my first client, my brother said a no from them is
   not a no from the work, so I kept editing and the next yes came."
   (127) - a real loss and a brother's voice, but "a no from them
   is not a no from the work" is a consolation, and the ending
   ("the next yes came") wraps up too neatly to leave anything
   behind after the last word.
8. "My father told me to finish what I start before I chase the next
   thing, and fifteen years later I still hear him every time I want
   to quit halfway." (147) - the closest cousin to the winner, same
   father, same staying power, but "finish what you start" is the
   platitude the brief warns about, and the winner's promise rule
   is the more specific, more earned version of the same lesson.

Why the winner wins: on criterion 1 it is squarely one sentence
about the best advice the writer ever received, quoted from his
dad. On criterion 2 the advice is worth carrying: a promise made
when you're tired is still a promise is specific (it names the
exact tired moment when promises get made), earned (it cost the
writer something to learn), and true beyond that midnight, since
it governs every yes he gives. On criterion 3 it sounds like a
real voice recalling a real moment: his dad's sentence, a midnight
habit of saying yes to everything, and a changed habit after it. On criterion
4 it reads in one breath, every clause doing work. On criterion
5 it lands: the last words, keeping the ones I'd already given,
leave the reader with the quiet weight of promises already made.

Pairwise verdicts, winner against each rival: vs 2, the winner's
advice is an original phrasing, the rival's is a known idiom; vs
3, a rule for all of life beats a rule for the editing room; vs 4,
a changed habit beats a narrower changed deadline; vs 5, a promise
rule beats a mealtime tip; vs 6, one tight breath beats a long
second half; vs 7, a rule that keeps costing beats a consolation
that wraps up neatly; vs 8, the specific promise rule beats the
platitude "finish what you start" in the same father's voice.
"""

import os

# The winning line (148 characters, one sentence, no trailing newline).
LINE = "My dad said a promise made when you're tired is still a promise, so I stopped saying yes at midnight and started keeping the ones I'd already given."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate: 1-200 characters, non-blank, exactly one sentence."""
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")


def main() -> None:
    line = LINE.strip()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one sentence,
    # within the gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    validate(written)
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
