import re
from common import re_pattern
from common import sys_argv
from common import name


def add_link(header, mermeid, footer):
    return header+generate_link_mermaid(mermeid)+footer


def del_link(header, mermeid, footer):
    return header+generate_nolink_mermaid(mermeid)+footer


def generate_link_mermaid(lines):
    P_pattern_object, D_pattern_object = generate_re_node_id_object()
    generated_lines = []

    for line in lines:
        generated_lines.append(line)
        P_result = P_pattern_object.search(repr(line))
        D_result = D_pattern_object.search(repr(line))

        if (P_result is None) & (D_result is None):
            continue
        re_result = P_result if P_result is not None else D_result

        generated_lines.append(generate_line(re_result.groupdict()))

    return generated_lines


def generate_nolink_mermaid(lines):
    P_pattern_object, D_pattern_object = generate_re_link_object()
    generated_lines = []

    for line in lines:
        P_result = P_pattern_object.search(repr(line))
        D_result = D_pattern_object.search(repr(line))

        if (P_result is not None) or (D_result is not None):
            continue
        generated_lines.append(line)

    return generated_lines


def generate_re_node_id_object():
    """
    下記のように|で繋ぐ手もあったがD側がgroupでの抽出（index）が少々複雑なるため、PとDを分けた
    ※P側は「P**」がgroup[2]に表示されるがD側は「D**」がgroup[9]に表示され、indexが分かれる

    pattern_object=re.compile(P_pattern+"|"+D_pattern)
    """
    P = re.compile(re_pattern.P_node_id)
    D = re.compile(re_pattern.D_node_id)
    return (P, D)


def generate_re_link_object():
    P = re.compile(re_pattern.P_link)
    D = re.compile(re_pattern.D_link)
    return (P, D)


def generate_line(result_dict):
    """
    generate line [click node_name "URL"]
    """

    github_url = generate_link(
        result_dict['node_id'], result_dict['node_name'])
    return f"{result_dict['space']}click {result_dict['node_id']} \"{github_url}\""


def generate_link(node_id, node_name):
    """
    https://github.com/アカウント名/リポジトリ名/blob/ブランチ名/リポジトリからの相対パス.git
    sample:https://github.com/lop9940/link_fix/blob/feature/action_yaml_add_test/README.md
    """

    repository = sys_argv.repository_name
    blob = name.blob
    branch = sys_argv.branch_name
    dir = name.P_dir if "p" in node_id else name.D_dir
    file = node_name+".md"
    return "/".join([repository, blob, branch, dir, file])
