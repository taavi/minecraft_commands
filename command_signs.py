import json

def make_sign(x, y, z, text, action):
    """
    e.g.

    >>> make_sign(-36, 67, -179, "bang" , "/tp @p -99 69 -149")
    /setblock -36 67 -179 wall_sign 5 replace {Text1:"{\"text\": \"bang\", \"clickEvent\": {\"action\": \"run_command\", \"value\": \"/tp @p -99 69 -149\"}}"}
    """
    print "/setblock {x} {y} {z} wall_sign 5 replace {{Text1:{json}}}".format(
        x=x, y=y, z=z, json=json.dumps(json.dumps({
            "text": text,
            "clickEvent": {
                "action": "run_command",
                "value": action
            }
        })))
