# Session 2, attempt 1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s: "OUZODYXAZV"

        t: "XYZ" duplicates are inlcuded so if Y apepared twice in t it it needs to appear twice in s

        res --> "YXAZ"
        so we actually want to return the minimum window. and the output is always unique okay

        substring so it must be continous here

        okay so lets think of brute force: 

        look at each subarray here O(s^2) at each subarray check if all letters of t are in s
            and that check could be O(t*s) as well?? is this a O(t*s^3) brute force. yeesh

            maybe we can make the check better if we have a count of each of the letters in t 
            and then make sure the counts line up at the end of going throguh s. that's len(s + t)
            okay so now we have (s^2 * s+t). can we make the subarray here better? well there's not biggest window here so sliding window with a fixed size doesn't make sense. but we can perhaps do a dynamic window.

        okay lets think here. 
        if we have the count of each number in t. 

        X : 1
        Y : 1
        Z : 1

        then we can have a live count of each substring we look at in s.

        the empty "" is 
        X : 0
        Y : 0
        Z : 0

        
        s: "OUZODYXAZV"

        t: "XYZ"
         
        we can't start two pointers on either end because we could potentially be removing part of the best minimum. so we def need to slide over s.

        so maybe we keep building up the window until it satisifes that 
        every val in our HAVE count is larger or equal to every value in our WANT count.

        when that happens, then we can update result if its shorter than our current result. maybe save indices so that we don't have to reconstruct the string each time (could be very long)

        if we reach a situation where our HAVE >= WANT and after updating, we should try shrinking until that's no longer satisifed. continue shrinking until that's not true. save the indices of the part before that last update of when its not true. oh actually that's the only time i shoudl really save, not everytime i grow and find a good substring. 

        s: "OUZODYXAZV"

        t: "XYZ"


        in order of how we look:
        res = ""
        O
        OU
        OUZ
        OUZO
        OUZOD
        OUZODY
        OUZODYX # found it!!! now shrink. all vals in have >= want
        UZODYX  
        ZODYX 
        ODYX # lost it, save the last subarray (res = "ZODYX"). then continue growing until we reach have >= want again
        ODYXA
        ODYXAZ # found it!!! all vals in have >= want, now shrink until not all vals in have >= want
        DYXAZ
        YXAZ
        XAZ # lost it, save the last subarray. then continue growing. (res = min(res, "YXAZ"))
        XAZV
        end of string. return res

        okay and now this sliding window is O(s) right. but our check is still O(s+t) each time. 
        can we fix check??

        yes!! we can make it constant and here's how. 
        so we can hold the maps right of have_map and want_map. 
        the issue is that each time we add a new character or get rid of one we update the map and check all vals. but really we need to only check that value if we know how many of the others ones satisfy. so then now we need an int. 
            have = 0
            want = 3
            if have == want we're good. 
            we increment have when we find a new val that's in t, and update the count in have_map and check against want_map. if they are == then we increment have. 
            once have == want then we are good. 
            we decrement have when we remove a val that's in t and decrement the count in have_map. if that val is now < the one in want_map. we decrement have. if have < want then we don't have all the numbers.
            since all we are doing is updating 1 map position, checkign against 1 val in the other map, and updating 1 integer and checking against 1 other integer that's O(1) check!!

            now we have a time: O(|s| + |t|) --> O(|s|)
            and a O(t) space compelxity for the map. 

            and as i said we can hold the integer value's instead of updating res so we don't keep building the string each time. 
            tada
        """
        if len(s) < len(t): # impossible
            return ""

        # build want_map and have_map
        # prob shouldn't do defaultdict(int) because later we ask if ltr in map and if we did defaultdict it would make a junk entry
        have_map = {}
        want_map = {} 
        for ltr in t:
            if ltr in want_map:
                want_map[ltr] += 1
            else:
                want_map[ltr] = 1
                have_map[ltr] = 0

        """
        OUZODYXAZV --> YXAZ
        XYZ

        want_map:
        {
            X: 1
            Y: 1
            Z: 1
        }

        have_map:
        {
            X: 0
            Y: 0
            Z: 1
        }

        0123456789
        OUZODYXAZV

        l, r = 0, 0
        want = 3, have = 0
        ""

        l, r = 0, 0
        "O"
        l, r = 0, 1
        "OU"
        l, r = 0, 2 
        "OUZ" -->  want = 3, have = 1
        .
        .
        l, r = 0, 6
        "OUZODYX" -->  want = 3, have = 3
            okay now lets shrink!!

        shrink loop
        "OUZODYX" --> saves [0, 6]
        "UZODYX" --> saves [1, 6]
        "ZODYX" --> saves [2, 5] # we make the udpate where we decrement have (bc of losing z here) soo this is the final res we save here. 



        """
        
        res = [-math.inf, math.inf] #large as possible
        l, r = 0, 0
        want, have = len(want_map.keys()), 0
        while r < len(s):

            # grow 
            while r < len(s) and have != want:
                if r < len(s) and s[r] in have_map:
                    have_map[s[r]] += 1
                    if have_map[s[r]] == want_map[s[r]]:
                        have += 1
                r += 1

            # shrink
            while have == want: # i don't think i need l < r
                # record l and r
                if res[1] - res[0] > r - l:
                    res = [l, r]

                if s[l] in have_map: 
                    have_map[s[l]] -= 1
                    if have_map[s[l]] == want_map[s[l]] - 1:
                        have -= 1
                l += 1

        if res[0] == -math.inf:
            return ""
        return s[res[0]:res[1]]





