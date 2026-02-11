class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for path in paths:
            part = path.split()
            root = part[0]
            for file in part[1:]:
                name , content = file.split("(")
                content = content[:-1]
                full_path = root + "/"+name
                hash_map[content].append(full_path)

        return [file for file in hash_map.values() if len(file) > 1]
        