import os
import re

from pynput import keyboard


def to_upper(st):
    return " ".join([s.upper() for s in break_up(st)])


def to_lower(st):
    return " ".join([s.lower() for s in break_up(st)])


def to_snake(st):
    return "_".join([s.lower() for s in break_up(st)])


def invert(st):
    ret = ""
    for s in break_up(st):
        if s.isupper():
            ret += s.lower()
        else:
            ret += s.upper()
    return ret


def break_up(st):
    strs = re.findall("([a-zA-Z][a-z]+|[a-z][A-Z]*|[A-Z]+)", st)
    print(strs)
    return [s for s in strs if s]


def to_camel(st):
    ret = ""
    for s in break_up(st):
        first = s[0].upper() if ret else s[0].lower()
        last = "" if len(s) == 1 else s[1:].lower()
        ret += first + last
    return ret


def rewrite(transformation):
    inp = os.popen("xsel").read()
    kb = keyboard.Controller()

    # clear selection
    kb.press(keyboard.Key.backspace)
    kb.release(keyboard.Key.backspace)

    #TODO: split string on punctuation we want to keep

    # re-write with passed transform
    inp = transformation(inp)
    for i in inp:
        if i == "\n":
            continue  # TODO: make this hit enter
        kb.press(i)
        kb.release(i)


def on_activate_1():
    rewrite(to_upper)


def on_activate_2():
    rewrite(to_lower)


def on_activate_3():
    rewrite(to_camel)


def on_activate_4():
    rewrite(to_snake)


def on_activate_5():
    rewrite(invert)


with keyboard.GlobalHotKeys(
    {
        "<ctrl>+<alt>+1": on_activate_1,
        "<ctrl>+<alt>+2": on_activate_2,
        "<ctrl>+<alt>+3": on_activate_3,
        "<ctrl>+<alt>+4": on_activate_4,
        "<ctrl>+<alt>+5": on_activate_5,
    }
) as h:
    h.join()
