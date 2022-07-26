import MeCab
import pandas as pd

class Paseri(MeCab.Tagger):
    cols = ["surface", "pos", "pos1", "pos2", "pos3", "form1", "form2", "base", "yomi", "hatsuon"]

    def __init__(self, options: str | None = None) -> None:
        args = "-Ochasen" + " " + options if options else "-Ochasen"
        super().__init__(args)

    def parse(self, text: str) -> pd.DataFrame:
        res = []
        node = self.parseToNode(text)
        while node:
            surface = [node.surface]
            feature = node.feature.split(",")
            if (feature[0] != "BOS/EOS"):
                res.append([*surface, *feature])
            node = node.next
        res_df = pd.DataFrame(res, columns=self.cols)
        return res_df
