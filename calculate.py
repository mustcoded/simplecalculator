class Calculate:

    def __init__(self):
        pass

    def cal(self, data,entry):

        if(len(data) >=3):
            ans = 0
            if data[1] == "+" :
                ans = float(data[0]) + float(data[2])
                data.clear()
                data.append(ans)
                entry.set(ans)
            elif data[1] == "-":
                ans = float(data[0]) - float(data[2])
                data.clear()
                data.append(ans)
                entry.set(ans)
            elif data[1] == "x":
                ans = float(data[0]) * float(data[2])
                data.clear()
                data.append(ans)
                entry.set(ans)
            elif data[1] == "\u00F7":
                if(float(data[2])!= 0.0):
                    ans = float(data[0]) / float(data[2])
                    data.clear()
                    data.append(ans)
                    entry.set(ans)
                else:
                    data.clear()
                    entry.set("0")