INDENT_WIDTH_PX = 20


def monospace(string):
    return "<samp>" + string + "</samp>"


def indent_string(string, depth=1):
    width = depth * INDENT_WIDTH_PX
    return f'<table style="margin-left: {width}px;" border=0><tr><td>{string}</td></tr></table>'


def mark_differences(value: str, compare_against: str):
    result = []
    for i, char in enumerate(value):
        try:
            if char != compare_against[i]:
                result.append(f'<font color="red">{char}</font>')
            else:
                result.append(char)
        except IndexError:
            result.append(char)

    return "".join(result)


def align_expected_and_got_value(expected: str, got: str, align_depth=1):
    width = align_depth * INDENT_WIDTH_PX
    got_marked = mark_differences(got, expected)
    return (
        f'<table style="margin-left: {width}px;" border=0>'
        f"<tr><td>Expected: </td><td>{monospace(expected)}</td></tr><tr><td>Got: </td><td>{monospace(got_marked)}</td> </tr>"
        "</table>"
    )
