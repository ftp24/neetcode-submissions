class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        isGroupedMap = {}
        GroupedList = []
        isRemoved=False
        for str in strs[:]:
            # check existing groups
            for list in GroupedList:
                isRemoved=False
                letterMapStr = {}
                letterMapCheck = {}
                if len(list)>0:
                    if len(str) != len(list[0]):
                        continue
                    
                    for x in range(len(str)):
                        letterMapStr[str[x]] = letterMapStr.get(str[x], 0) + 1
                        letterMapCheck[list[0][x]] = letterMapCheck.get(list[0][x], 0) + 1
                if letterMapStr == letterMapCheck:
                    list.append(str)
                    strs.remove(str)
                    isRemoved=True
                    break

            # add it to a new group
            if isRemoved==False:
                group = []
                group.append(str)
                GroupedList.append(group)
                strs.remove(str)
        return GroupedList
