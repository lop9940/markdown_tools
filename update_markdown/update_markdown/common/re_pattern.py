P_node_id = "(?P<space>\s*?)(?P<node_id>p\d+)(?P<node_start>\(\[)(?P<node_name>.*?)(?P<node_end>\]\))"
D_node_id = "(?P<space>\s*?)(?P<node_id>d\d+)(?P<node_start>\[/)(?P<node_name>.*?)(?P<node_end>/\])"
P_link = "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>p\d+)(?P<node_start>\s\".*?\")"
P_link = "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>d\d+)(?P<node_start>\s\".*?\")"