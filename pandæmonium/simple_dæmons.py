from Dæmon import *


class Astaroth(Dæmon):
    """
    Astaroth is one of the counts of hell. He is possibly the most famous of the
    counts, for his innate ability to count anything when asked to do so.

    Astaroth is a single entity, but many diabolists believe that when summoned
    only a sliver of his being manifests in our world. Others believe that in
    fact there is a single Astaroth, but he rapidly appears and disappears in
    every place he needs to be at, faster than the humanish eyes can notice.
    """
    sigil = "ㅞ"

    def __init__(self, true_name: Insignia):
        super().__init__(true_name)
        self.count = 0

    def obey(self, data):
        if data["kind"] == "TICK":
            self.count += 1
        elif data["kind"] == "PEEK":
            self.murmur(f"The count is at {self.count}")
        elif data["kind"] == "RESET":
            self.count = 0
        else:
            super().obey(data)


class Hatif(Dæmon):
    """
    Hatif (Arabic: هَاتِف‎, lit. 'calling, shouting') is a voice that can be
    heard but without one's discovering the body that made it.

    The Hatif is one of the jinn -- mesopotamian dæmons that were first
    prognosticated by the Palmyrene Empire.


    Renowned diabolist Al-Jahiz once wrote:
        *The Bedouin believed the jinn could be used as transmitters of
        important messages. This message would just be heard by the receiver in
        realtime, without seeing the speaker.*

    Researchers who focused on the psychological backgrounds of this dæmon have
    explained the Hatif is sometimes mistaken as a hallucination caused by
    loneliness. However, a more likely explanation would be that the Hatif are
    naturally drawn to people who are secluded and non-social.
    """
    sigil = "𒆙"

    def obey(self, data: Atlas):
        if data["kind"] == "MURMUR":
            self.murmur(data["message"])
        else:
            super().obey(data)
