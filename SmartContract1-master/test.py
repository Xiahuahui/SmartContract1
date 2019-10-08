for nodeChoice in nodeChoicesB:
    if flagB:
        cComb = ChoiceCombination()
        cComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
        newChoiceB.append(cComb)
    else:
        T = 0
        for cComb in ChoicesB:
            if cComb.needNode(node, "B"):
                if str(T) in ChoicesBFlag:
                    del ChoicesBFlag[str(T)]
                newcComb = copy.deepcopy(cComb)
                newcComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
                newChoiceB.append(newcComb)
            T = T + 1
