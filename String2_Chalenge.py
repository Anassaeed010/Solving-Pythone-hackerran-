from collections import Counter

if __name__ == '__main__':
   s = input().strip()

   words = s.split()
   ctr = Counter(words)


for key, item in sorted(ctr.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(key, item)