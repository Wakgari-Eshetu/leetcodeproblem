class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_map = defaultdict(int)
        for item in cpdomains:
            num , domain = item.split()
            num = int(num)
            parts = domain.split('.')
            for i in range(len(parts)):
                full_domain = ".".join(parts[i:])
                hash_map[full_domain] += num
            
        return [f"{num} {domain}" for domain, num in hash_map.items()]