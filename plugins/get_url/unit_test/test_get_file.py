import os
import sys

from unit_test.util import Util

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_get_url.actions.get_file import GetFile
from komand_get_url.actions.get_file.schema import Input
from unittest.mock import patch
from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


class TestGetFile(TestCase):
    def tearDown(self):
        Util.clear_cache()

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFile())

    @patch("six.moves.urllib.request.urlopen", side_effect=Util.mocked_request)
    def test_get_pdf_file(self, mock_get):
        actual = self.action.run({Input.URL: "https://test.com/v1/test.pdf", Input.IS_VERIFY: False})
        expected = {
            "bytes": "JVBERi0xLjUKJe+/ve+/ve+/ve+/vQozIDAgb2JqCjw8IC9MaW5lYXJpemVkIDEgL0wgMTUwMDcgL0ggWyA2NzggMTI1IF0gL08gNyAvRSAxNDQ3NyAvTiAxIC9UIDE0NzI2ID4+CmVuZG9iagogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo0IDAgb2JqCjw8IC9UeXBlIC9YUmVmIC9MZW5ndGggNTAgL0ZpbHRlciAvRmxhdGVEZWNvZGUgL0RlY29kZVBhcm1zIDw8IC9Db2x1bW5zIDQgL1ByZWRpY3RvciAxMiA+PiAvVyBbIDEgMiAxIF0gL0luZGV4IFsgMyAxNCBdIC9JbmZvIDEgMCBSIC9Sb290IDUgMCBSIC9TaXplIDE3IC9QcmV2IDE0NzI3ICAgICAgICAgICAgICAgICAvSUQgWzw0ZGFjMTgxZWIxMGU1NjljYjc5MzBhYmQzYmJkMzZlMT48ZjhmNGE2YjlmNzU2MmEzMzMzNzI2MTQzNjc5NjMxNDA+XSA+PgpzdHJlYW0KeO+/vWNiZO+/vWdgYmA4CSTvv73vv71YRkDvv73vv70W77+9Kgbvv73vv70BCT3vv70E77+9LgMT77+9dyAJBkY0AgDvv70GLgplbmRzdHJlYW0KZW5kb2JqCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo1IDAgb2JqCjw8IC9QYWdlcyAxNCAwIFIgL1R5cGUgL0NhdGFsb2cgPj4KZW5kb2JqCjYgMCBvYmoKPDwgL0ZpbHRlciAvRmxhdGVEZWNvZGUgL1MgMzYgL0xlbmd0aCA0OCA+PgpzdHJlYW0KeO+/vWNgYGBlYGBa77+9AATvv71ZDHAAZTMDMQtCFO+/vRbvv70ZGO+/vRnvv73vv71S77+977+977+9du+/vX9hAADvv73vv70F77+9CmVuZHN0cmVhbQplbmRvYmoKNyAwIG9iago8PCAvQ29udGVudHMgOCAwIFIgL01lZGlhQm94IFsgMCAwIDU5NS4yNzYgODQxLjg5IF0gL1BhcmVudCAxNCAwIFIgL1Jlc291cmNlcyAxMiAwIFIgL1R5cGUgL1BhZ2UgPj4KZW5kb2JqCjggMCBvYmoKPDwgL0ZpbHRlciAvRmxhdGVEZWNvZGUgL0xlbmd0aCAxMTggPj4Kc3RyZWFtCnjvv71tzbsO77+9MAxG77+9PU/vv70ZYu+/vRvvv71pViQY77+977+9AUPvv73vv73vv73vv71Q77+977+977+9Uy4j77+9d++/ve+/vTHvv73aoVDvv73vv71LTzYTdO+/vQzvv70cM0MSWe+/vUN3GVvvv70ydE9/77+9PUUKAO+/ve+/ve+/ve+/ve+/vUJ1Du+/vQjvv71N77+977+977+9NO+/ve+/ve+/ve+/vSEkZRVQSO+/vV7vv73vv70Ab3Jbcy/vv73vv70i77+9CmVuZHN0cmVhbQplbmRvYmoKOSAwIG9iago8PCAvRmlsdGVyIC9GbGF0ZURlY29kZSAvTGVuZ3RoMSAxNTc4IC9MZW5ndGgyIDEwNzc4IC9MZW5ndGgzIDAgL0xlbmd0aCAxMTgxOCA+PgpzdHJlYW0KeO+/ve+/ve+/vQVU77+927ItDO+/vTXvv71LQ++/ve+/ve+/ve+/ve+/ve+/ve+/vUATaO+/vXEITgjvv70JEO+/vQLvv73vv73vv70dAu+/vV3vv73vv70je++/vXvvv70+77+977+977+9eG8wRu+/vc2qWe+/ve+/vWrvv71a77+9FO+/vRpMYu+/vQ7vv71AaQcw77+977+977+977+977+9HyDvv73vv73vv73vv70KYGXvv71gZmVlR++/ve+/ve+/vQRB77+977+9MiNTawPvv71dQA5g77+9fxAk77+977+9Zu+/vVfvv73vv70Z5JWn77+9AAbIu++/vQHvv704AGzvv73vv71sPO+/ve+/ve+/vQB2Vlbvv73vv70hOjjvv70DJO+/ve+/vUDvv70AJWbvv73vv70DGO+/vUwt77+977+977+977+9DO+/ve+/ve+/ve+/vR7vv70/77+9ADoLegAbHx8P77+9X++/vQAxe++/vTPvv73vv70MDFAy77+977+9AO+/vV9P77+9MO+/vQNoOFjvv73vv70Q77+977+9SkEnaAPvv7048rOwuO+/ve+/vTPvv73ZuzA7OFsL77+9MwLvv71BEBvvv70677+9Be+/ve+/vQbvv70E77+9aRjvv71sZg/vv73vv70zZmRq77+977+9De+/ve+/vW/vv73vv73vv70V77+977+977+9GQh4NdiBLO+/vWDvv73vv70IV++/vSXvv70Z77+9ejhAQ04R77+977+9CATvv71NVu+/ve+/ve+/vQjvv73vv71sAGzvv71s77+9Tu+/ve+/ve+/vT/vv71A4L+C77+9LCwc77+9He+/ve+/ve+/vSDvv70177+9CmQHBO+/vUgrMkM8IO+/vQAz77+977+9H++/ve+/ve+/ve+/ve+/vWvvv73vv73vv70Z77+977+977+977+977+977+9V++/vWYAaTE177+977+9a++/ve+/vWrvv73vv73vv70Z77+9CHFhdgHvv73vv71p77+977+9T++/ve+/vSlL77+9LSUc77+977+9YO+/vQvvv73vv70kQe+/vUDvv73XsXvvv73vv71977+9H++/vQ7vv71g77+9fwErEO+/ve+/ve+/vU8T77+977+977+9LFpg77+977+9K1BO77+9X++/vVcT77+9f2zvv71ACO+/ve+/ve+/ve+/ve+/ve+/ve+/vQMAdAIAPSxsWO+/ve+/ve+/ve+/vXQE77+977+9ZO+/vWN+77+977+977+977+977+977+9EWDvv73vv70E77+9F2QFfO+/ve+/ve+/ve+/vWLvv70GBEDvv71d77+977+977+977+9dO+/vTdCZmMDWO+/vSwgAHPvv701CO+/ve+/ve+/ve+/vWbvv73vv73vv73vv73vv73vv71BHgAD77+9V++/ve+/vQFY77+977+977+977+977+977+9VV7vv70OYDvvv73vv73vv73vv73vv71fFmkFOT0Zde+/ve+/vTvvv73vv71PXO+/ve+/vQPvv73vv73vv73vv70KYGLvv71iBe+/ve+/vREZ77+977+977+9f++/vVE1A++/ve+/ve+/vX/vv73Kge+/vRwAfH9X77+9Ou+/ve+/ve+/ve+/ve+/vV8C77+977+977+9cu+/vQPvv70777+977+9w6tq77+9AO+/ve+/ve+/vdyQ77+977+977+977+977+977+977+977+9We+/vX/vv73vv73vv70p77+9T++/ve+/ve+/ve+/ve+/vXdB0q52dn/vv73vv73vv73vv73vv71/77+9Zu+/vSA777+9fxFeRe+/vQp5XQAl77+977+9NQDvv71v77+9Du+/ve+/vVUCWu+/vVzvv73vv73vv71XDmLvv73vv70IYmBr77+9f++/vRHvv70iDe+/vQBa77+977+9IBY2f++/ve+/vW/vv73Wny3vv70D77+977+977+9Di7vv70/77+9Cu+/ve+/ve+/vWrvv73vv73vv71177+9LD7vv70+HS7vv73vv73vv73vv70FfN2c77+9PlIKbO+/vWDvv71n77+92Lnvv70BZu+/ve+/vWbvv73Ir++/ve+/ve+/ve+/vQDvv71s77+977+9aAnvv73vv71L77+9ABZm77+9A++/vTUE77+92p4v77+977+977+9Ge+/vc+N77+977+9AFjvv73vv73vv73vv71Cfypg77+977+9B2QD77+9AO+/vQHvv70BLFbvv73vv71/EO+/vR9eDgDvv73vv70/ICfvv73vv73vv73fkO+/ve+/vRV5Otq8Pibvv71h77+977+977+9Ge+/vQtg77+977+9D3zvv70w77+9f8icfADvv73vv71H77+9H++/ve+/ve+/vR3vv70BX09z77+9R2nvv73vv71777+9Be+/vWtaFu+/ve+/vc6vD++/vV96fh3vv73vv73vv71eJyDvv70DaO+/ve+/vTjvv71gIRBsWxPvv71yWyVG77+9zrQ9JjRN77+977+977+9Su+/ve+/ve+/ve+/ve+/vXrvv73vv73vv71EX++/vRnvv73vv718Le+/vTTYhe+/ve+/vSlFdyXvv71E77+977+9fe+/vVjvv73vv70pQe+/ve+/ve+/ve+/ve+/vSROfXLvv70ZeWEC77+9bzzvv71Q77+9ey8pEgnvv73vv73vv73Pk++/ve+/vXbvv70H77+9Ru+/vXZ577+9XCdXXnTvv70v2Lfvv709Mh7vv717S++/vUdC77+977+9dirvv70VUB5L77+977+977+977+9Ig0D77+977+9UO+/vWfvv70SUO+/vUPvv71IEe+/vWPvv71577+977+977+977+977+977+977+9GX8h77+977+9Y0Dvv70977+977+9KO+/ve+/vV9n77+977+977+977+9Wi3vv71kd++/vSDvv70i77+9JyDvv73vv73vv70a77+977+977+9Fu+/vUvvv73Hn++/vS4qWO+/vVvvv71oFCwg77+9QWNMWWHvv71g77+9Y8+oBO+/vUfvv73ru6vvv71GFu+/vdi2cu+/vQDvv73vv73vv71977+9Wwnvv73vv73vv704Js6UKu+/ve+/ve+/vSYR2JBq77+9D0DSvTYr77+91ZZr77+9Tivvv70U77+9Je+/ve+/ve+/vS/vv70ZND3vv71D77+977+9Tu+/vVrvv73vv73vv73vv70+77+977+90JTvv73vv73vv73vv73vv73vv71OX++/vW8i77+9IiTvv73vv71s77+9bAzvv71X77+977+9M0hT77+9SiDvv71vOnTvv71yOBjvv71Lbknvv73vv71wZiHvv73ege+/ve+/ve+/vURsG++/ve+/ve+/ve+/ve+/vXDvv73vv70jJCdc77+9Pu+/vdG+77+9dWfvv71t77+9M++/ve+/vXbvv71YRkEvQe+/ve+/vS/vv73vv70pZ2fvv73vv702HFLvv73vv73vv710eRlS77+977+977+9fu+/vdCqCe+/vQDvv71m77+9Sljvv73vv73vv73vv70l77+9Pe+/vRXvv70377+9Fu+/ve+/ve+/vQo477+9ZO+/ve+/ve+/vSsG77+9DQM9be+/ve+/ve+/vTLvv71o77+9azXvv71yfVXvv73vv70677+9YBrdqwsYEA8K77+94bu277+927guLRU377+977+9d9C+Oyt3DxMf77+977+977+977+9E++/ve+/ve+/vU3vv70/77+977+9RSVNRizvv71N77+977+977+9bDfvv73vv73vv71jTXE3Cu+/ve+/ve+/ve+/vTrvv71C77+977+977+9He+/ve+/ve+/vSVy77+91LQF77+9Su+/vQrvv73vv73vv718Fu+/vRYkC++/vQnvv73vv71F77+9Pl/vv73vv73vv73XtO+/ve+/ve+/vUHvv71mYu+/vUZTZ++/vSzDvDNpHe+/ve+/vT5/JhIn77+90Lzvv73vv73vv71rHe+/vXt+anTvv71ieHLvv73vv73bru+/ve+/vRtnTwNA77+9KzIN77+9Lu+/ve+/vWJ+77+9P++/vXJN77+9LjLvv73vv70q77+94aeW77+9WO+/vRJJde+/vUwfcO+/vWhgBFbvv70dQisHK++/ve+/vdiRLCDvv73vv70277+9YgED77+977+9XELvv73vv71X77+977+9PXlM77+9UO+/ve+/vWHvv71P77+9K++/ve+/vVIh77+9Dj1o77+9NUnvv70w77+9A++/ve+/ve+/vUfupJwpD++/vTw1cH8pcXo477+9Fu+/ve+/vXouMe+/vWJ+Elnvv70dCu+/ve+/vSA7He+/ve+/vWbvv70fPUXvv71V77+9biDvv73vv70eZgQi1Kbvv70sLe+/vUBNTO+/vTrvv70q77+9VB5FMBN/NSYt77+977+977+9GO+/ve+/ve+/vUpm77+9xZ4aCe+/vTEoeUgJFE3vv703D3wsdzXvv70A77+97omO77+977+9Oe+/vVnvv73vv70I77+977+9IXTvv715a3dKae+/ve+/vRjvv71z77+9MCrvv73KlwAHNe+/ve+/vd2xFBTvv71J048/BO+/ve+/ve+/vVjvv719EO+/vV4E77+977+977+9T2vvv73vv70WMn8O2pzvv73vv70NXivvv73vv71H77+977+977+977+977+9EBkkNBXvv73vv71JPu+/vUMxGcmFM0hq77+977+977+9UBXvv71k77+9Je+/vRTvv73vv73vv73vv71CLe+/vUUT77+9Tmts77+9dVZwZe+/ve+/vXhI15Lvv73vv70D77+977+977+977+9Qu+/vWsm77+9fe+/vT0J77+977+9P1rvv71RG++/vTnvv73vv70bNjXvv71w77+9cO+/vVEYZO+/ve+/ve+/vTV977+9Ou+/vV7vv73vv73bt2MRQcS6Rlp677+9JH/vv73vv73vv73vv71aNhLvv73vv73NvUbvv704Z3jvv70NeO+/ve+/vTTvv71O77+9QSh0A++/ve+/ve+/vTnvv73vv73vv73vv73vv71AcDBI77+9yYgvM++/ve+/vW0WJu+/vS8u77+93YpMRu+/vUzvv70e77+9QBvvv73Nru+/vTrvv73vv71S77+9Le+/vUpFZe+/ve+/vX9f77+977+977+977+977+9bu+/vUFwOAMcHe+/ve+/ve+/vSdCJFQY77+977+9Ye+/ve+/vU4077+977+977+9dCM/Qu+/ve+/ve+/ve+/ve+/vVHvv73vv73vv73vv73vv73vv71rfFrvv70Z77+977+977+977+977+9C++/vXrvv73vv71KJ1/vv73vv73Hiu+/vUR677+9KiTvv71Z77+9Ewzvv73vv73vv70yPO+/vc6B77+904gUb0bvv73vv73vv71+AO+/vWse77+977+9Ju+/vVDvv71aKhtKNGTvv70t77+9XM+N77+9Fu+/vXvvv73vv73vv706UShaTlVsEjscfu+/vWLvv71m77+9HBAXEu+/ve+/vX1/TO+/vRrfqe+/ve+/ve+/vXVHdXw3ce+/ve+/vU/vv71T77+9Pjnvv73vv73vv73vv73vv70vdiPvv73vv73vv701QO+/vcmT77+977+977+977+9W9e9PHHvv70TaXh877+9OjZ0xIVkS++/ve+/vQFP77+977+977+977+977+9AFJp77+977+9YAJFMO+/vcaFO00x77+977+9dFVl77+977+977+9bRHvv70B77+977+9AG3vv70W77+977+9U++/vdyj77+977+9fe+/ve+/ve+/vQoWAD3vv70NRu+/ve+/vWLvv70eFw5UV++/vUEzQO+/vXR0YO+/vSNa77+9MxtaTu+/vV9u77+9Yk7Nuu+/vQrvv73vv73vv70077+9EO+/vScvYS3vv73vv73vv707y67vv71aVe+/vT3vv73vv71MW++/vV5DXO+/vWVH77+9BO+/vQvvv71EIlvvv73vv73vv71N77+977+9QO+/ve+/vXAHCt2777+9BV0477+9NHw8JWIEVCpUMO+/ve+/ve+/ve+/vUM8Zmfvv70mPt2W77+977+977+9G3Pvv71nPwUfByUUE++/ve+/vRQdzLVn77+977+9VjTvv70t77+977+9F27vv73vv73vv71q77+977+9GzNINjnvv73vv70K77+9YR5LFu+/ve+/vTl577+9Dw5P77+9d2nvv70Wb++/ve+/ve+/vSdkeu+/ve+/vVYNYO+/ve+/vV7vv73vv73vv70j77+977+977+977+977+977+9Su+/vUop77+977+9K++/ve+/vQvvv73vv70xOu+/vSTvv73vv73vv73vv73vv73vv70rGgPvv70gQsa804Dvv73vv71O1bHvv70a77+9Clrvv73vv73vv73vv71hSlpV77+977+977+9WhVhJ++/vT1uYQsJTAzvv71077+977+9MO+/ve+/vS9/77+977+9Vu+/vWnvv73vv71c77+9Be+/ve+/vSED77+9GO+/vR3vv73vv73vv73vv73vv73vv71sEu+/vRsSXO+/ve+/vWPvv70jTRnsvIkQb++/vWo3c++/vSbvv71W77+977+9HETvv71r77+9Zm7vv71e77+9Wu+/ve+/vSZVOe+/vTh977+977+9bGTvv71L77+977+977+977+9KmPvv70Y77+977+9He+/vUMF77+9V0tG77+9Au+/ve+/vTjvv73vv73vv73vv70FFu+/vVpGw6bvv73RsCpU77+9Ve+/ve+/vUHvv70t77+977+977+9c2RBR92hIe+/vTlC77+9QuuilO+/ve+/ve+/vQrSt++/vXnvv70P77+9cW3vv70B77+9dnR277+9Fe+/vVlL77+9U++/vVHvv70UDXsl77+9ybPDhu+/ve+/ve+/ve+/vTjvv73vv73vv71GPgJK77+9Nu+/ve+/vQsa77+977+9FADvv71d77+9Pxx/ce+/ve+/ve+/vQDvv71777+9dSIi77+9f++/ve+/ve+/vSNR77+977+9IjTvv73vv708K3FGCS/vv71SEu+/vSzvv70W77+9JO+/ve+/vUcl77+9CHrvv71JEFvvv70m77+9Be+/ve+/ve+/ve+/ve+/vSTvv70UI++/vVJ3Ie+/ve+/ve+/vX3vv70677+977+9Ei0mRjDvv70W77+977+977+9c++/ve+/vQvvv71u3a3vv73vv718Le+/ve+/vRjvv73vv73vv73vv712EE3vv70X77+9AAXvv70zIW46CwgJ77+9OO+/vWTvv71N77+9Je+/ve+/ve+/ve+/ve+/vSUmWzDvv73vv70B77+977+977+9fGHvv73vv73RuO+/vQphE3MtL++/vUJ1FBtnNu+/ve+/ve+/ve+/ve+/vW7vv73vv71gAe+/vRTvv70oA++/vQhsSCRHalZReinvv70o77+9Pm7vv70KMO+/vTga77+9exBi77+9be+/vSAb77+9cklV77+977+977+9Je+/vWLvv73kmKw0Ju+/ve+/ve+/ve+/vTrvv73vv73vv70jE0Pvv73vv73HnjxhM13vv711Ze+/vXRlOO+/vVzvv73vv73vv70UFjhj77+977+9Gu+/ve+/ve+/vUZ2aO+/vVzvv73vv73vv70ZYE11CcScGyDvv73vv71h77+977+9GD/vv73vv71LWQNYP++/ve+/vUXvv715aHte77+9LWFOZlEa77+977+977+9SO+/ve+/ve+/ve+/ve+/ve+/vRMt77+9NDQu77+9eu+/ve+/ve+/ve+/vVnvv73vv70zFS7vv71BT++/vVzvv73vv73vv70HUmIp77+97qaIF2rvv73vv70I77+9Ku+/ve+/vWnvv73vv70dBzMJdgHvv73vv71077+9KAvvv73Kl++/ve+/vQLvv70KLO+/vcu6Hu+/ve+/ve+/ve+/vTEe77+93rfvv70L77+9Fe+/vSVt77+9Ygdj77+977+977+9dBTvv70J77+977+9xKBJSO+/ve+/vWjvv71/77+9WW8d77+977+9VUsY77+9LnBQbe+/vdmY77+9DO+/vSrvv71t77+977+977+977+9aO+/vVHvv73vv7070o9y77+977+9BE1r77+9WU7vv7125Lykc8ev77+9WHA077+9Mn3Vn1hPLgpvFe+/ve+/vWlM77+977+9GkLvv73vv73vv71VbOeFskM1w65z77+9Xe+/vRrvv71377+977+9Z++/ve+/vXXvv71S77+9MAd7aFTvv73vv73vv70077+977+9Kkvvv73vv71nSe+/vVo1Uu+/vWDvv73vv71aUhfvv73vv73vv73vv70V77+9Ju+/vXnUnu+/vTLvv73vv73vv73kq5JpUH7vv70G77+977+9d++/vSYF77+977+9SkQG77+977+977+9IwPngozvv70B77+977+9Xu+/vWM9J++/vW9L77+9AglqQe+/vc2C77+9J++/ve+/ve+/ve+/vWPvv73vv71aUl/vv70u77+9I8+mFe+/vTpm77+977+9Ru+/ve+/ve+/vQlD66uJ77+977+977+9W1zvv71Qf++/vXpJ77+977+9MCjvv73vv73vv71pe8y1GQNn77+9VhPvv73vv73vv73vv70s77+9de+/ve+/ve+/vT7vv73vv71177+977+9WUtjAe+/ve+/ve+/vWDvv70V77+977+9UBDvv71F77+9a3Zz77+9J9KR77+977+9Se+/vRXvv73vv73Wls+MP2Tvv73vv73vv70CH3zvv707NlXvv73vv71q77+977+9bO+/ve+/ve+/vQfvv73vv73vv73vv70Y77+977+9ce+/ve+/ve+/vdK077+9M++/vTdbKu+/vR/vv73vv73vv73vv73LiUsSTlfvv73vv70FWH8N77+9fVrvv71Q77+9zZDvv73VmUMG77+977+977+9d++/ve+/vRwKIu+/ve+/vQR577+9N++/vQUi77+977+977+977+977+977+9U++/vR1WfDDKuu+/vWPvv73vv73vv71q77+9JRXTpO+/vXXvv73vv71MBu+/ve+/ve+/vWM7LFbvv71bO2xU77+9xo8Z77+977+9e++/vcyDPe+/vT8Y77+977+977+977+9PO+/vdyC77+9f++/vdSIe1UMfe+/vQnvv73vv70u77+9NtOCCO+/ve+/ve+/ve+/vWrvv71T77+9Lu+/ve+/vVcKXu+/ve+/vXx777+977+977+9TwTvv73vv70UCMiI77+9PO+/ve+/vUh677+977+9GkYf77+9Q3LepO+/ve+/ve+/vTnvv73vv73vv70lIO+/vSdn77+9Ue+/ve+/ve+/vdWHSycG77+977+977+93Z8US++/ve+/vRnvv70FWt2qenDvv73Lhu+/ve+/ve+/vRwg77+9PO+/vQosy5Dvv73vv71g77+9YVNy77+977+977+9Wu+/vXzcue+/vSVrSDldagB/y5Y877+9dmzvv73vv71877+9V++/vSjvv73vv70j77+9LO+/vXRZ77+977+9AnMS77+9w5rvv71377+9B++/vRojOkTYoGLvv713NEHGpe+/vSHvv73vv71c77+977+9z4gb77+9Ju+/ve+/vd6z77+9HlRHGO+/vTbvv71v77+9de+/vVMU77+92KMubkzvv70ubmbvv71+77+977+977+9JHdeL++/ve+/ve+/vUvvv71bJe+/ve+/ve+/ve+/vTLvv71pOAJ2dHPvv73vv706Yu+/ve+/vQcW77+977+977+977+977+977+9PArfn++/ve+/vSfvv73vv700OiTvv70DJVtzau+/ve+/vVTvv71r77+9dt+OQO+/ve+/ve+/vVvvv73vv70GZu+/vRfvv71I77+9RRfvv73vv73vv73vv73vv70YJu+/ve+/ve+/vSsBXe+/vWhtKu+/ve+/vRAxZTgmRTRwckTvv70I77+977+9Tzxj77+977+9ZWvvv73vv73vv73vv73vv714fTECUe+/vWRVE++/vUUK77+9fu+/vXEDe35077+977+9V++/vTUgCyfvv73Zte+/vTnGhRLvv71+77+977+9CO+/ve+/vXVXV3Dvv70SJe+/ve+/vUFI77+9au+/vXjFvwXvv73vv73vv73vv70VPe+/ve+/vSjvv70eJEXvv70qMyQw1oTvv73vv73vv73vv70m77+977+9P++/vSZt77+9WTbvv71A77+9YO+/vRMxeGHvv701AGLvv70o77+977+977+977+9A++/vRolSkF277+977+977+9ce+/vSoIENmK77+977+9Yu+/ve+/vWDvv70g77+977+977+977+977+977+9DDjvv71G77+9fRTvv73vv71UPllpaSg4yY7vv71877+977+9Cu+/ve+/vQk477+977+977+9Yu+/vcyl77+9A++/ve+/vQQM77+977+977+9Xl7vv71pFi7vv71c77+977+977+9OF3vv73vv70a77+977+977+977+927Pvv73vv73vv70IHkcLMEkx77+977+977+9dHQAdUcxAy3vv70477+977+9XTTvv71D77+9QO+/vWdRIFXvv71wRO+/ve+/vSEk77+9OCJnRO+/vQHvv712A3h3Od2Eae+/vT5i77+9Fu+/vWhT77+9x7Qd77+9Ue+/ve+/ve+/vdOMC++/ve+/ve+/vSdTPDshQO+/vQcbRWIEWzzvv73vv70H77+9FxEi77+977+9H++/ve+/vTZJR++/vXzvv70ZJ++/ve+/ve+/vR1UPygpa++/ve+/vQvGpgvvv70zbu+/ve+/vUoy77+9DnPvv73vv73vv73vv71cZWXvv73vv73vv73vv73vv70l77+9HgHvv73vv73vv71377+977+9S++/vVUX77+9WHrvv73vv70tae+/vQzvv73vv73vv71677+9L++/vXIWUO+/vRrvv700yYIvcC3vv70n77+9QDcwFC92QO+/vXQg77+977+9dnUJR++/vVnvv70Y77+977+9Z++/vSbvv73vv700A07vv70F77+9V++/vTPvv73vv71A77+9ce+/ve+/vc+/WO+/vXw51pIzDu+/vQvvv703KWXvv73vv70x77+9d2nvv73vv71cJhFm77+9dXXvv73vv718H++/ve+/ve+/vRvvv7166qKMUe+/vWfvv71tR++/vSlk77+9TiNUZF8QB0fvv73vv71N77+9fkQI77+9fe+/vRnvv73vv73vv73bkG9w77+9Q++/vQkwWnnvv71M77+977+9UO+/vXbvv71W77+9RiTvv70rTTBY77+977+977+977+977+9eO+/ve+/ve+/vVw077+977+9IAsp3azvv73WnwknTe+/ve+/vSI8dO+/ve+/vUEH77+9Vu+/ve+/vSIG77+9Ge+/ve+/vdu7Ze+/ve+/vQnvv73vv73vv73vv73vv70p77+977+977+9Gzfvv70K77+9Jlo577+977+9J++/ve+/vWrvv73vv73vv73HvO+/vWnVru+/vSPvv73vv70v77+9Uu+/ve+/ve+/vUJj77+9Znvvv70oAQs277+9Kh9gTO+/ve+/vU8yNh1v77+9Ue+/vXldPVfvv73vv70v77+9Vy/vv71c77+977+9fC3vv73vv70Z77+9Oj0/Ujzvv70a77+9Zu+/vRPvv712HO+/vWsx77+9Q++/vUFy77+9d0Dvv73vv70X77+9bSohPe+/vXQVJkDvv73vv719Umnvv73vv71n77+9CXg877+9Mte977+9HiYZ77+977+9X++/vT1eQe+/vSEZ77+977+977+977+9MVrvv71uCx1QZGgTXu+/ve+/vQTvv73vv73vv71R77+977+977+9ypobDT8477+9CCp0D++/vUVa77+9ce+/ve+/vW/vv70577+9b0hB77+977+9K++/vQFW77+9QU8fGtSZDzPvv73vv73vv71o77+977+97ZmxaEc1Nu+/vSTvv71HFu+/vTwf77+9CXgS77+977+9Xe+/vUl8L++/vd+vM++/vVEp77+977+9ZSLvv73vv71wW++/ve+/vVbvv73vv70W77+9Ejnvv73vv70eNe+/vXHvv73vv73vv73vv73vv73vv73vv70cHGbvv70gKe+/ve+/vQjPsGNVYu+/vWdDRXpf77+9C20keu+/vXRn77+9YDzvv70o77+9cC3vv71VCu+/ve+/ve+/vX/vv70M77+9Je+/ve+/vXQqVu+/vWElFu+/ve+/ve+/vQlyLe+/ve+/vVrvv73vv71o77+9PD3vv73vv73vv71z77+977+9J++/ve+/ve+/veaPiVrvv70kQ1Av77+9WQUk77+9QTBRD++/vUpiGXHvv70377+977+9Su+/vQfvv71sNu+/ve+/vQxm77+977+977+9IGrvv70S77+9Ke+/vRMGY++/vWgqFO+/ve+/vVJt77+9Ww8m77+9UAky77+9eO+/vRFB77+977+9H++/ve+/vRNW77+9Lu+/ve+/ve+/vRbvv71L77+9W++/vVzvv71F77+977+977+9DVkHVe+/ve+/ve+/vQbvv73vv714V++/vXvvv71eFEPvv71T77+9Pu+/ve+/ve+/vW7vv714fm8mW++/vUXvv73vv73vv70i77+977+977+9H++/ve+/ve+/vVbvv70N77+9D2zvv70ROe+/ve+/vUrvv71ebXrvv73vv70SN++/vQlL77+977+95IOp77+9WR5W77+9AFrvv71B77+9WDjvv73vv71U24hU77+977+9Lnfvv71O77+9IzMyYu+/vTzvv70d0IXvv71ZMD7vv73vv73vv71Q77+977+977+977+977+977+9be+/vV4/77+977+9O++/vTo/77+9ENK277+977+9XO+/vVNZ77+977+90b3vv70r77+9RO+/vS4j77+977+977+9Iu+/vRt2ee+/ve+/vR3vv70UJ2kG77+9Pu+/ve+/vSrvv70KA0xr77+977+977+9TO+/ve+/ve+/ve+/ve+/vQ/vv73vv73vv70077+9DTfvv70ZGz5+fh/vv70777+977+9Nu+/ve+/vUjvv73vv70q77+9Ye+/ve+/ve+/vWdw77+9AyVS77+977+9Ny3vv70W77+977+9S++/vQPvv71R77+977+977+9WO+/vVrvv73vv73vv70077+9bmzvv71777+91Ybvv73vv73vv70377+977+9W++/vQxYX++/vXDvv73vv70bde+/vXIWyabvv71+yZjvv71IN++/vXBSBDrvv71k77+9ah1ffkTvv70p77+977+977+977+9ET7vv73vv73Lv0zvv70F77+9Zu+/vWkqKhfvv73vv73vv73vv70MVRdkYe+/vTwp77+977+977+977+9c++/vS7vv71/77+977+9J++/ve+/vTvvv73vv71rce+/vSTvv73vv73vv73vv73vv70DA++/vWLvv73vv73vv73Rt2Tvv70B77+9XxQdE92U77+977+9NXjvv70777+977+977+9KhFJ77+977+9Tm3vv73vv71Iae+/vRbvv73vv73vv71RGUp377+977+9G++/vRHvv73vv73vv73vv73vv73vv73vv73ztqm477+9ajTvv70077+9MD/vv71bJu+/vVBMee+/vRzvv71277+9K++/vQE1Tnt9dO+/vX3vv70n77+9b++/vS3vv70477+9yLDvv73vv71bJu+/vW7vv73vv71Q77+9VO+/vQ07eA1tE++/ve+/ve+/ve+/ve+/vU7vv73vv73vv70rWO+/vRgi77+977+9cQPvv71K77+977+977+9U1oQFe+/ve+/vRfUsTHvv71SagkTfu+/ve+/vTLvv73vv73vv70XcO+/vVhbUn7vv70n77+977+9Se+/ve+/ve+/ve+/vTcJ77+977+9Ae+/vT7vv70B77+977+9PRQr77+977+9N++/vV/vv70TVX0F77+977+9Ke+/vVsU77+977+9343vv71p77+91qNL77+977+9G++/vRI977+9GO+/vSTvv73vv70S77+977+9CO+/vSF177+9HO+/vQMkDXsC77+9ZF1n77+9X++/vXrvv70mUmnvv73vv704Bu+/vQU877+9NUTvv71zXO+/vWvvv73vv73YmmMeL1M3QO+/ve+/vRBY77+977+977+9VF5OMknvv73vv71/BnQRehhVNcK3CO+/vW/vv73vv71077+9Ge+/ve+/vWXvv73vv71wOe+/vWEY77+977+9TUgLYDAq77+9FO+/vWLvv73vv73vv70N77+977+977+9Ou+/vS5kZ0Z/T++/vXfvv71o77+9H++/vS5I77+977+977+9Ku+/ve+/vSBo77+9du+/ve+/vVYL77+977+9N9us77+977+977+9B++/vXJaNUpL77+977+977+9LDMvfO+/vXxDb++/vQE377+9RBYCdu+/vX1iRAnvv71Xbu+/vcKd77+977+977+9XXnvv73vv73vv70S77+9Dgfvv73vv73qmrk+77+9aO+/vTJE77+977+9ADl+fu+/ve+/ve+/vWUa77+9L++/ve+/vSTDozMqCEYr77+9J++/vVY377+977+977+9U++/ve+/ve+/vVvvv705DG45FEPvv73vv73dlWvvv71H77+9QW3vv73vv70377+9wrPvv71877+977+9WH3vv73vv70MKe+/vRdwEU8577+977+977+977+977+9B13vv73vv70z77+9YEYW77+9Q++/vVTXiu+/ve+/vWLvv71477+9Bj5qFWTeu++/vVfvv71ZY++/vQ/vv70677+977+9W9q+K2jvv71c77+9De+/vUFw77+9Rynvv71scXFAY2oU77+9R1bvv73vv73vv73ZpCzvv71R77+977+977+9Zu+/ve+/vX4b77+9f++/ve+/ve+/vRMS77+977+977+9R3Hvv71WAzvvv73vv73vv73fqmTWvu+/vVvvv70Y77+9ae+/vdyZBgp777+9EGHcnO+/vXfvv73vv73vv73vv71H77+9TMOV77+9eGTvv70kF3gWR0sE77+977+9d29977+977+9IW3vv71s77+9fRli77+977+977+977+9FR3vv70Vz4Qj77+9bl3vv70K77+9Pu+/vUgX77+9Ie+/vUnvv70/Y2Mz77+9Ux8z1IJrDVZ+Cmp177+977+977+9Bi4t77+9WDBcU++/vVcjHSs377+977+9a3Dvv73vv70GdX7vv73vv70qyabvv73vv73vv73vv71u77+977+977+937Lvv71lbF7vv73Tiwjvv71MV++/vQoQ77+9Dl9277+9R++/vRse77+977+9GWLvv73vv71M77+9XN6t77+9VSBYEErvv73vv70iIGYpJ0Fs77+9Ehbvv73vv73vv71kC++/ve+/ve+/vTIc77+977+9eDvvv70U77+977+977+9Se+/vX40QO+/ve+/vXB+Ve+/vUBjWzVi77+9Qu+/vUTvv70277+9B++/vWfvv70e77+977+977+91Ijvv70p77+9woTvv70qTyd+Jdmx3pbvv70gU++/ve+/vSDvv73vv71S3LxR77+977+977+977+9HCosKO+/vXN2akHvv73Gne+/ve+/vTswNsa/77+9Nu+/vUfvv73vv73vv73vv73vv73vv71b77+977+977+9LHR077+9DCbvv70C3YMO77+9HRDvv73vv70TRu+/ve+/ve+/vV7Dvu+/vRpG77+9Qu+/vSbvv73vv714Ae+/ve+/vTQBLWrvv73vv71qBe+/ve+/vQbvv73vv71vVBzvv710VO+/vUvvv70t77+9fu+/vRPvv71S77+9zqfvv70ZE1Xvv73vv70q77+9VO+/vUjvv70LUENWRu+/vULvv71Z77+9djQYGnQ677+9DBrvv73vv70AaO+/ve+/vR/vv71k77+935lP77+9Iu+/vX/vv73vv71D77+9Eu+/vS4hG0jvv71VTu+/ve+/vW7vv73vv73vv73vv71l77+9cHtn77+9K++/ve+/vQktUS/LoQbvv73vv71GHu+/ve+/vWIcQe+/vTHvv73vv73vv71BQ++/vdGbAwXvv73vv715fu+/vQTvv73Xughx77+9EEnvv73vv73vv70INDJYIu+/ve+/vX0a77+977+977+9Au+/ve+/vSXvv71SOAUnS2I8Y1E/YG/vv70Y77+9Ju+/vVRAC++/vQ3vv73vv71EX++/ve+/vVdr77+977+9WO+/vUrvv73vv73vv71n77+9R23vv70977+9Cu+/vVAFRA9FaApd77+9du+/ve+/vW3vv73st7Hvv73vv73vv73vv71l4qSK77+9cz7vv73vv710Au+/ve+/vSrvv71icu+/vSrvv70977+9WWjvv71QUe+/ve+/vRNt77+9QV8JV++/vRcp77+977+9YAHvv70fae+/ve+/vTwd3Kp4K10T77+9TS5q77+9H++/ve+/ve+/ve+/vTtZ77+9IXpDQ1Xvv70m77+977+9T03vv71eYe+/vUUU77+9He+/vVRN77+977+9BCpV77+9du+/vU7vv71SGUhMTe+/vXPvv70OdO+/vQBuBTwQNnzvv71u77+977+977+9TlUgFO+/ve+/vWtJRO+/ve+/vXgv77+977+9MSvvv73vv71WK++/ve+/ve+/vUTvv71gFe+/ve+/vWLvv73vv71u77+977+9du+/vSdPQH7vv70j77+9x4Tvv73vv71nXl3LmmHvv70177+977+977+9Tu+/vWl877+977+977+9KX7vv70i77+9ai7vv73vv73vv73vv73vv70vT++/ve+/ve+/vTfvv70CBAhoVGttF0Tvv73vv70EIkPvv70s77+977+9K1piXe+/ve+/vVZx77+977+977+9e++/ve+/ve+/vVvvv70sVFHvv71d77+9Lu+/vQoD77+977+9SO+/ve+/vUR177+9Bu+/vW3vv70iP++/vRnvv706bQvvv71U77+977+9LxF/77+9xLYT77+977+9fh9177+977+9L++/vW7vv73vv71b77+977+9WsSCZe+/vWPvv73vv70Y2bEL77+9O1Xvv73vv70kAO+/vduUFu+/ve+/vXPvv73vv73vv70M77+9Lu+/vUMq77+9Cz9HQe+/vVHvv70wVO+/vU1777+977+9Y9SyOVPvv70G77+977+9OQYc77+977+9Mu+/vTPvv73vv73vv70W77+9DQzvv71M77+977+977+9XO+/ve+/vV3EuO+/vT46zaHvv71G77+977+9We+/vWrvv73vv71p77+977+9Ae+/vc6Ub1dVfDbvv71CKWbvv70K77+977+977+977+977+9Vn05LMS677+977+977+9F++/vX5D77+9C07vv73vv73vv73vv73vv70M77+9IO+/vQTvv71w77+977+9am/vv71MBO+/vXNYEe+/ve+/ve+/ve+/vVvvv711d2Hvv73vv70FWu+/ve+/vQTvv73vv71O77+9EEbvv70477+977+9ITvvv71tHR8iPX7vv73vv70p77+9STc577+9D++/ve+/vQHvv70677+9DmsAXSk977+9PGvvv73vv73vv71V77+977+977+9Vu+/ve+/vVUWYO+/ve+/vU8777+9IsyBVUTvv73vv73vv71377+9Y++/vXV6Je+/ve+/vU3vv70/c34jDHzvv71+77+9ae+/ve+/vSdA77+977+9IO+/vUPvv73vv73vv70cOHrvv73Sl++/vTTUklY577+9cO+/ve+/vXLvv71Q77+9FTXvv71Z77+9fO+/ve+/ve+/vdSt77+9WSLvv70lRu+/vR8b77+977+9Ou+/ve+/vR7vv71s77+977+9IC5hL2Dvv73jmII577+977+977+977+9dFLvv73vv71o77+977+977+977+977+9Ce+/vSVEKh0Y77+977+977+9S++/ve+/ve+/ve+/vScGO++/ve+/vWM977+977+977+977+977+9Ve+/vRMUH2/vv73vv73KlO+/ve+/vc+Z77+9A++/vT/vv73vv73Su3nvv73vv73ilZDvv73vv71sXO+/vWHvv73vv73vv73vv70F77+9cO+/ve+/ve+/vdm3Ue+/vWDvv70Zbe+/vSTvv71XZ3Hvv73QoyhMNiBAMu+/vU3vv71bz4zvv73Ni++/vR3vv71+77+9PA/vv73vv73vv73WjkUuLu+/ve+/vUbvv71j77+977+9FE7vv73vv73vv701yLXvv73vv73sr5Z+Eu+/vT7Sre+/ve+/vVTvv73vv73Qje+/ve+/ve+/vTHvv71oKu+/vWUDfUBMUe+/vSPvv71S77+977+9ee+/vQ3vv73vv73vv71v77+9z65N77+9fsSY77+977+977+9PFnvv70QTO+/vRfvv73vv719SEXvv71ofgjvv71EKO+/vQfQsygP77+977+9G0zvv73vv73vv71pdyl077+977+9dm3vv70277+9HhPvv70YdO+/vUEz77+9KlTvv70x77+977+977+977+977+977+95YGe77+9Snfvv70877+977+977+977+9K27vv71AXDRR77+9dVheOu+/vU9E77+977+977+977+977+9PiN877+9bu+/vXF+77+9fu+/vRIk77+9ZtGcH++/ve+/vTnvv70j77+9QWTQje+/vUPvv71SVu+/ve+/ve+/vXTvv73vv73vv73vv73vv71ufB/vv73vv70377+9ee+/vW8K1qLvv73vv71cH++/vXHvv73vv71lRREx77+977+9Hu+/ve+/ve+/vd+777+9AmHvv73vv73vv71m77+977+9IVXvv73vv73vv71u77+9X3JE77+977+977+9RCM977+9O++/ve+/ve+/ve+/vQduGe+/vQYoJQDvv70c77+9XlZDee+/vVTvv73vv73vv73vv70tee+/ve+/ve+/vWjvv71j77+977+9D++/ve+/ve+/vQ8O77+9IAfvv70k77+9Jm0U77+977+9B2FtOe+/vSzvv73diO+/ve+/vdCQ77+9PO+/ve+/ve+/vcmMCknvv71w77+9eu+/vWPvv73ElDkY77+977+977+9PV1u77+977+9MT3vv73YnHnvv70V77+977+9aAYh77+9GSbvv70477+9SG7vv70VOu+/vcKYz4RS77+977+9U++/ve+/ve+/vRfvv70B77+977+9CDnvv714X++/vXE2BSbfqm/vv73vv73Zty/cvSbvv73vv71nVO+/vcS1AO+/vUnvv73vv73vv71QBjQ5JO+/ve+/vUlF77+977+926gb77+9YBppDhct77+9Zm/vv70d77+9fC3vv70aVBpSbnRDJEXvv70E77+9W++/ve+/ve+/vTDvv71eP++/vU5EShjvv73LtO+/ve+/vR5O77+92Kl977+9ae+/vQ0gO++/vUsgT1zvv707S14K77+977+977+977+977+977+977+9e20W77+9Y3o1M2Mh77+9Dz8q77+9MO+/ve+/vTXvv719JypSDR1I77+977+9M++/vVVg77+977+9Su+/vVvZoR7vv73vv73vv71gHe+/ve+/vTnvv73vv70/77+9Qhhq77+9Ru+/ve+/ve+/vQbvv73vv70wSHpCPVUv77+977+9BwTvv70sV2jvv71nUWrvv70F77+9WBXvv73apTxB77+977+9Cu+/vRx4Ilzvv73vv71z77+977+977+9OO+/vTYp77+9Ku+/vdqTfTQJ77+9y4Fj77+977+977+977+9Bzs+fO+/vQ/vv71VFjZc77+9EUoDNkrvv71q77+977+9TO+/vTQ1ZTILUe+/vSzvv70j77+9Ge+/vV0kHR3vv70Q77+977+977+9SFUhGu+/vTMtYu+/vWtK77+9DO+/vQ/vv73vv71VU++/vTzvv73vv73vv73vv70L77+977+977+977+977+9K3JaYPSHu5ZaI++/ve+/vQp877+9fe+/ve+/vXvvv71mKjHvv73vv71AFO+/vWnvv70f77+9SUR+H++/vULvv71VQe+/vcaQ77+9Yu+/ve+/vTzvv70pDu+/ve+/vWcG77+977+93L4yEe+/vSxa77+977+9OxVXSO+/ve+/ve+/vWJHaUnvv73vv71/LAbvv70TN++/vSbNphPvv71ZZHPvv71N77+977+977+9WO+/ve+/vSRGzK9xN2Pvv71+bzNz77+9NgLvv73WsNW6VGRi77+9X++/vUckZnhGWxIM77+977+9We+/vQnvv70GZnN4Cu+/ve+/vWs1Xu+/vT8gdjvvv73vv73vv73vv71j77+9Xe+/vXrvv73vv73vv73vv71v77+9XO+/ve+/ve+/vd+J77+977+9fBLvv70yKxjvv71JG++/vRZdSloK77+977+977+9zLXvv73vv70W77+9Ve+/vWHvv70I77+9DO+/ve+/vXzvv73vv73vv73vv73an++/ve+/ve+/vWnvv71X77+977+9VRfvv71yUu+/ve+/ve+/vVwWMO+/vULvv70v77+977+9Ak0L77+977+9QEjvv70s77+977+9QGrvv71Z77+9O3ZhBO+/ve+/ve+/vW4jai1z77+9KxBZfO+/vVDvv70d77+977+9A0vvv73vv709Q++/vWjvv73vv71W77+977+9D++/vdub77+977+9de+/vRll77+977+9xIFcVFMH5qSJDTU+LQFS77+9cxkY77+9Z9i077+977+977+9P1fHri3vv73vv71IYTlIECrvv73vv73vv70z77+977+9HndEHH/vv73vv70i77+9S++/ve+/vUvvv73Pg++/vRHvv73vv71f0pwpOWoAcHbvv71lRR3vv71qO1rvv71Kfj1A77+9xYnvv73vv71k77+977+9au+/vVgE77+977+977+9KO+/ve+/vSPvv73LrRtLYFTvv73Fnu+/vXjvv71GJu+/vSB6RO+/vQ/vv70ccEd6GO+/vSDvv70BTu+/vQHvv73vv73vv73vv73vv71kFO+/ve+/vcioYBTvv73vv71QWAXvv707xK4077+9LSd3GhBIK++/ve+/vUR0CUoD77+9YX9N77+977+9IWY3fzzvv73vv71bIO+/ve+/vVnvv73vv73vv70Vd++/vXfvv70WSCtEYwjvv71J77+9bH7vv73vv73vv71q77+9Dg3vv73vv70Z77+9Pe+/ve+/vX/vv71SEse1XO+/vQ9D77+9yKTvv70777+977+977+9OGjvv70BSO+/vUvvv73vv71bblbvv70VZlAp77+977+9XCdrSu+/vQ7vv71NY++/vQTvv73vv71T77+9cn1377+9fj54Zhvvv71G77+9NWPvv73vv73vv71hQ1zvv73vv73vv71077+9Ce+/vXHvv73vv71wBu+/vRVi77+977+977+977+9K++/vVNvNRTIuO+/ve+/ve+/vRnvv73vv73vv70dKyha77+91aQZ77+977+9Yu+/vU0b77+9G++/ve+/ve+/vWjvv71G77+9ADnvv73Oku+/ve+/vQDvv70177+977+9Ee+/vTrvv70g77+977+9MSnvv73Nj++/vdyI77+9SSLvv70fFhPvv70+77+9de+/vQ5LJQXvv73vv71mSO+/ve+/ve+/ve+/vWDvv71vVDjvv70477+9TQnvv71a77+977+9Zg9X77+9WH3vv71WZiwp77+91IwY77+9DjIHOyvvv719c++/ve+/vSoQXu+/vca7Fmvvv73KoEZdPElJYkTvv73vv70OCkvvv73vv73vv73vv73vv71dOu+/vSdYe281Z++/vUw9Qu+/ve+/vRBwSBdye2Lvv70YWmTvv70E77+9Pu+/ve+/vRZHKu+/ve+/ve+/ve+/vSXvv73vv73vv71g77+9Xe+/ve+/vU/vv70+77+9E++/vSPvv71E77+9Ku+/vVkm77+977+9V++/vX7vv71pD++/vXwk77+9NHAmCh8577+9KUsV77+9b++/ve+/vXAaBVoU77+9z4Lvv71y77+977+9DO+/vQJrVDvvv73vv71S77+977+9K++/ve+/vRtA77+9d++/ve+/vQ3vv73vv710F1Hvv70H77+9zZrvv71wxKLvv73vv73vv71F77+9D3Ub77+977+9Yu+/vW42LdSLEO+/ve+/vSBSa1l+77+9bxRCHO+/vW3vv73vv71R77+936VrRO+/ve+/ve+/ve+/vUTvv73vv73CtzQw77+9Eu+/ve+/vTtg77+977+9cGVOZ++/vWbvv73vv70sLhPvv71r77+977+9Re+/ve+/vVFn77+977+977+977+9el9eCtGv77+9cS3vv73vv73vv71Hae+/vX1y77+9DSvvv73vv73vv71T77+977+977+9V++/ve+/vSBc77+977+977+977+977+9bQrvv71g77+977+9Bu+/ve+/vVXvv73vv73vv71n77+977+9K29uQRTvv702UO+/vWIaQWhOMt21YkPvv73vv73vv70H77+9RyBXAXPvv71N77+977+977+9Ou+/vRPDn++/ve+/vULfr++/ve+/vXzvv71P77+9Fu+/vWbvv70R77+9O++/ve+/vVndslzvv70I77+977+9UO+/ve+/vcWcUDxRJHpv77+9PFrvv71X77+9R++/vTrvv71lFhXvv702AWXvv73vv73vv73vv702Ie+/ve+/ve+/vVwX77+9b9Gr0YYgOca3Q++/ve+/vWnvv73vv73vv70T77+92qbvv73vv73vv70EfRHvv73vv71YKO+/vShPNG4f77+977+977+9KO+/vVJ0N3ZN77+977+977+92Y7vv718FVo577+977+9UO+/vTdR77+977+9Rjjvv73vv70bejjvv73vv71nZO+/vQJUUULvv73vv71O77+9Ue+/ve+/vXvvv73vv73vv71G77+977+9Qu+/vRfvv71OI9eK77+9CSvvv73vv70kM++/vWPvv73vv70PCu+/vVRm77+9ehPWtO+/vRDvv70oX++/ve+/vR/vv70BWO+/vWXvv73vv71Z77+977+977+977+9x48D77+9fQhjciTvv73vv73vv71277+9NO+/vXPvv70QR++/vWwa77+9HAXvv73vv73vv73vv70AXe+/ve+/ve+/vVppO2Uw77+9PUVM77+9fw/vv73dhlpo77+977+977+9PVswSO+/vRJCOjnKkkdwd++/vUzPn++/vWLLnEdh77+9KRFe77+977+977+977+9dhUD77+977+9MO+/vXxJ77+977+977+9Ie+/vUfvv73vv71NPHjvv70qJUDvv73vv73vv70y77+9dnPvv70F77+9x6kCaVc577+977+9C1cLRBPvv73vv71e77+9LQVc77+977+9UCnvv710X1bvv708yY1377+9aGBk77+9ElJ277+9Z8ug77+9Su+/vcOQ77+977+977+9Ou+/vU4qyJg377+9PwNgMlfvv73vv73vv73vv73vv73vv70nEu+/vSnvv73vv73vv73vv71+Du+/vUFw77+9fltc77+9Cu+/vQhl77+977+977+977+9Z0Tvv73vv71S77+9G1pU77+9Y++/vU8n77+977+9MQPvv73vv73PgSrvv73vv73vv73vv71m77+9D3Hvv73vv70H77+9WnlHKu+/vTXvv73vv70N77+977+977+9Mjrvv73vv73vv71BLgN8Q++/ve+/vXM277+9Xu+/ve+/vTbvv73vv73vv71S77+977+9N++/vSINUXrvv706Du+/vXlLV++/vRPvv70c77+9RTnvv71h77+9b++/ve+/vX05M++/vSfvv70d77+9G++/vcW377+977+977+977+9WTw177+9TQfvv70wAhPvv73vv71v77+9Q3sr77+9ce+/vfClsKzvv73vv73vv719cWbvv71177+977+977+9S++/vU7vv73vv73vv71X77+977+9a++/vXZ277+977+9ZGTvv71R77+977+9IFnfij9/Iu+/vQnvv715aGrvv73vv71SDFrvv70n77+977+977+9V++/vVBAB3F+fjLvv71L77+9b++/vQ/vv70B77+9JTgp77+9R++/ve+/vXfvv73vv70QQO+/vWQqcXVCNXhuwp8Iwpfvv71p77+9e1bvv73vv70a77+9Z++/vRvvv73vv70G77+9au+/vUzvv71u77+9JO+/vUAV77+90KPvv71KLe+/vWMN77+977+9Be+/ve+/vQPvv71477+9Eu+/vXbvv73Si++/vXdY77+977+9R++/vRLvv70M77+9He+/ve+/ve+/vVDvv71EU++/vSrvv73vv71E77+9Rm9SCEU777+977+977+977+977+9YO+/ve+/vWbvv710We+/vSzvv73vv71pfHzvv73vv71VfRLvv73vv70t77+9AFsi77+977+977+977+977+977+9JO+/ve+/vWF577+9NBFAaGNQ77+92ZHvv73vv73YsB/vv73vv73vv73vv73vv73vv70GzbXvv73vv71v77+977+9XV12djvvv71WDzwHEGDvv73vv70CGnLvv70k77+9SBDvv71n77+9Tu+/ve+/vXsqBO+/vShJ77+9bGVdRiLvv71iHu+/vWXvv71SMO+/vRPvv73vv73vv73vv73vv70G14VNae+/vUHvv73Yqu+/vT/vv70aR++/vcu5HO+/ve+/vRjvv71O77+9RXDvv71PNO+/vTbvv71Y77+90Zfvv73vv70/Fe+/ve+/ve+/ve+/vXHRs8WXVXY4DHkPG35C77+977+9IH/vv73vv71l77+977+977+9L++/ve+/vWMoLBjvv73vv73vv714WH5O77+9xKnvv73vv73vv73vv70sDiXvv706FO+/vUNY77+9ElLvv700eHpTF++/vSnGuxbvv73vv73vv71BK++/vSBM77+977+977+9SO+/ve+/ve+/vTpH77+977+977+977+9cu+/vUMZ77+977+977+9D2ZoSe+/vXvvv73vv73vv73cpu+/ve+/ve+/vTZh77+91rcxUO+/ve+/vWLvv73vv70W77+9c1NS77+977+9wp9X5oKPD++/vWnvv73vv71i77+9EO+/vXnLu0rcl++/ve+/vX3vv73vv73vv70777+9JlJM77+9FO+/ve+/vUQ777+977+9cQ/vv70SUEzvv71G77+977+91pjvv73vv71c77+9M++/vXgw77+977+9P29hJe+/ve+/ve+/ve+/ve+/vS/vv715URnvv73vv73vv73vv73vv73vv73vv70QTB/ToO+/vTYi77+977+977+977+977+9Gzbvv719CO+/ve+/vX0DNu+/vWJpaEA477+977+977+9Y++/ve+/vSvvv73vv70O77+977+977+9fO+/vTrvv719Wg1d77+9Ne+/vdO0ZN6Q77+9ZVzVpwnvv73vv73vv713De+/vT/vv71UOFXvv73vv73vv73vv73vv70v77+9UWXvv73vv73vv703Vu+/vVdn77+9FO+/vQ8KT++/ve+/ve+/vVzvv71Tc++/ve+/vSzvv73vv73vv70377+977+9Vu+/vXoMYmgK77+9fe+/vUx8G++/vWkkfO+/vTfvv73vv70lIu+/vS9CKjlI77+977+9GFoR75OD77+977+9R9aN77+977+9UDnvv71677+9UO+/ve+/ve+/vR/vv70i77+9JDAC77+91L9/Q3Xvv73vv73vv73Hpu+/vVkcQxNCVFbvv71J370U77+9FQsX77+9VykgZO+/vRcr77+9Yu+/ve+/vX/vv73vv73vv73Tj25777+977+9ByzpurHvv73vv71p77+9dhtxde+/ve+/ve+/ve+/vWXvv70Q77+9x5BDRVLvv71KLu+/vdm51LckZe+/vQnvv73vv73vv73vv718V0Tvv71YYhzvv70be829f2vvv71777+9Pu+/vW0SHe+/vUvvv71H77+9RE5oCCzvv73vv71YGDFiCDTvv73vv70W77+9DO+/ve+/ve+/vRvvv70nVANmRe+/ve+/vXjvv700bATvv70k77+977+977+9b0vvv71zc++/ve+/ve+/vQNT77+977+977+977+9Qu+/ve+/vV1uLO+/ve+/vSl+Ee+/ve+/vV8Z77+977+9WzcXDu+/vUDvv73vv73vv73vv73vv73vv73vv73vv70t77+977+9G3vvv73vv71/GO+/ve+/ve+/vUbvv73Qq++/vXU9EO+/vXMDH++/vWh+77+9NO+/ve+/ve+/vTofYS3vv70tNe+/ve+/ve+/vQrvv70J77+9FUDvv73vv73vv71XXt+hKO+/ve+/vVHvv70lTe+/vUJSS2VM77+977+9PH/vv73vv73vv71Z77+9E++/vWElI++/ve+/ve+/vSxNbO+/ve+/vXPvv73vv73vv73ctcSR77+9R1Dvv73vv71YJO+/vVvvv73vv71T77+977+977+9Ne+/vUYjUDXvv70O77+977+977+9Fnfvv73vv73vv70+dgnvv73vv71iB2lUzLXvv73vv71yVi3vv73vv71ZM0Xvv70377+9D++/vWg677+9Tu+/vW/vv73vv73vv73vv70h77+977+977+977+977+977+9V++/vVDvv73vv73hmZsS77+9JAfvv73vv71ZQe+/vUrvv71JD++/ve+/vRted10BTwxP77+977+9I++/ve+/vTBGbe+/vQU777+977+9fGPvv71O77+9Ku+/vSnMtA/vv71L77+9ZGnvv71uXe+/ve+/vVbCgiLvv71BOj9A77+9DBPvv73vv73vv73vv73vv71QQ2QJ77+9Eu+/vSpweO+/ve+/ve+/ve+/vV/vv73vv73vv71N77+977+977+9ZeKBie+/vdmEOGfvv70T77+977+977+9KO+/vQjvv71kPAlBFSZF77+9F8W777+977+977+977+9aE/vv71T1b9nXO+/vWwM77+9chzvv73vv70b77+977+9F3QtSkdFMCzvv71O77+977+9D3rvv73vv73vv73vv73vv70P77+977+9IO+/vT9HMdebE++/vRVRQ++/vSvIvQxD77+9a++/vWs427Xvv70v77+9YyQe77+9I++/ve+/vUjvv73vv70OPe+/vUtO77+9Ru+/ve+/ve+/vRHJhHE4Xlzvv73vv73vv73vv70Y77+977+977+977+977+92b5k77+977+977+9T++/vdOzJWnvv73vv70977+977+977+9BCvvv703SO+/ve+/vcSo77+9WTHZlu+/vQ9Yx7Xvv70z77+9K++/vWbvv73vv71LQzrvv71977+9YVdN77+9FX1677+977+9HwPvv71O77+977+9Ve+/ve+/vUbvv71QIO+/vQ1k77+9Pu+/ve+/vVjvv71w77+977+977+977+9dO+/ve+/vXnvv71kJO+/vVwj77+946qr77+9c++/vQPvv73vv73vv73vv70W77+9KCoDV2VNb++/ve+/vXrvv71MZwXvv73vv71YHw/vv71FM++/ve+/vX/enu+/ve+/ve+/ve+/ve+/ve+/ve+/vRJN77+9HXXvv71xce+/ve+/vSXMh++/vTYXDnwMPAHGie+/ve+/vWBd77+977+977+977+977+977+977+977+977+9d++/ve+/ve+/ve+/vTXvv73vv73Vqe+/ve+/vUbvv73vv73Yu++/ve+/vdK677+9UO+/vV7vv70n77+9FmVeUF/vv73vv73vv73vv73vv70z77+9be+/vXQsQO+/ve+/ve+/vVDvv7174ZeX77+9WV3vv73vv73vv73vv73vv70Hzovvv73vv70fFkrvv71077+9zJIt77+9ZURnC03vv73vv73vv70Y77+9Hu+/ve+/vTldb3Fn77+9Kjnvv73vv70k77+9Hhvvv70P77+9b2tI77+977+977+9T++/vQjvv70077+9Ulp6Se+/ve+/vXRDVu+/ve+/vWzvv73vv73Npy1zdF9IZe+/ve+/vTgw77+977+9GDpnau+/ve+/vVtIyqXvv73vv70I77+9OExo77+9P11H77+9OgplbmRzdHJlYW0KZW5kb2JqCjEwIDAgb2JqCjw8IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlIC9MZW5ndGggNzQwID4+CnN0cmVhbQp477+9bVXvv71u77+9MBTvv73vv70r77+977+9Su+/vWI7JO+/vQoh77+9Ce+/vTjvv70q77+9au+/ve+/ve+/vW4kSO+/vSQc77+977+977+977+9I++/vWx7AO+/ve+/ve+/ve+/vTPvv71g77+9fu+/vWwn77+9bO+/vWYSPnLvv71q77+977+977+9FWbvv73vv73cte+/ve+/vV3vv70U55Op77+9X8aU77+9HGfvv70n77+977+9Ne+/ve+/vQzvv70+77+9ZO+/ve+/vRoeLHlTF++/vXNpRu+/ve+/vSRt3qvvv71T77+9D++/vX8zfybFqRN877+9P1fHoe+/vScc3LdqOFrvv71377+977+977+977+9Te+/ve+/vSXvv71N77+9V03vv73vv73vv70j77+977+9Fu+/vXXvv702J3jvv73vv71FB++/ve+/ve+/vQ5VXXYXMWwPae+/ve+/ve+/ve+/ve+/ve+/vTJy77+977+977+9HgYWbz/vv73vv73vv70277+977+9Ce+/vUs2fe+/ve+/ve+/ve+/vX0477+9D++/ve+/ve+/vStNV++/ve+/ve+/ve+/vUbvv73vv73Znu+/ve+/vWjvv73vv73vv71g77+9Yu+/vTnYhu+/ve+/ve+/ve+/vcmw77+9dwbvv73vv73vv73vv73vv70w77+9xoJUFU1p77+9dlfvv71uV++/ve+/vWDvv73vv73vv70t77+9fBXvv73vv73vv71vLu+/vRXvv73vv71ITSzvv73vv73vv70V77+9aBUsZWjvv73vv71R77+9Fu+/vQImQ03vv73vv70t77+977+977+9ERUsDu+/ve+/ve+/vThR77+9YHHvv71MMO+/ve+/vWjvv70Feijvv71Q77+977+9LlbXqCDvv73vv73vv73vv73vv73vv73uop3vv70LLO+/vWgsJe+/ve+/vSXVoe+/ve+/ve+/vTXvv73vv73vv70aOO+/vR04cEzvv73vv73vv73vv73vv73vv71C77+9FO+/ve+/vSQTce+/vQ/GqR8vMO+/ve+/vTjvv71477+977+9P3Lvv73vv70aeO+/vXkQIe+/vULvv73vv70977+9BFgSF++/ve+/ve+/ve+/ve+/vQzvv71577+977+977+9OA8y77+9VkHXoHDvv70i77+977+9Au+/ve+/vVrvv71x77+9eO+/vTh0B2t4Ec6b77+977+9X++/ve+/ve+/ve+/ve+/vVPvv704a++/vUhg77+977+977+977+977+9bhvvv73vv73vv71rzIAT77+977+9HVJPBU5IPUNwQjojDT3vv70lAjjvv73vv704ETjRmu+/vUJD77+977+9L++/vTnvv70hyagOfkLvv70MfRLvv73vv73vv71ScdKJ77+9VO+/ve+/vUZJ77+9GxXvv73cqO+/vc+N77+9fG5U77+9c++/vRLvv70b77+9fG4UZUVB77+977+9eHfvv73vv73vv71Jfe+/vQfGn++/vQF/77+977+977+9Se+/ve+/vXnvv73vv71r77+9dO+/ve+/vWc+Tzrvv7150rHPk05877+977+977+977+9SS9877+977+977+9ee+/ve+/ve+/vUnvv70+Tzrvv71577+9a++/vSfvv73vv70877+977+977+9KRU+T++/ve+/vXlKZ++/vTtz77+9fO+/vUvvv73bhHfvv73vv73vv70V566zD++/vXts77+9Q++/vSfvv73vv73vv73vv709bu+/vRbvv73vv73vv70977+977+977+9Bkbvv71577+9D++/ve+/vVAKZW5kc3RyZWFtCmVuZG9iagoxMSAwIG9iago8PCAvVHlwZSAvT2JqU3RtIC9MZW5ndGggNTIyIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlIC9OIDUgL0ZpcnN0IDMyID4+CnN0cmVhbQp477+9dVNZa++/vUAQfu+vmMeWYu+/vd6SIARiB++/vSFtCe+/vXsR77+977+977+9G0nvv71IRlIg77+977+977+977+9Ve+/vU3SgjTvv73vv73NsTNcAAMuQSvvv73vv73vv70G77+9Bu+/vUhnIO+/ve+/ve+/ve+/vRnvv71rR++/vQzPnS/vv70V77+977+9A++/ve+/vV3vv73vv70j77+9Envvv70E77+977+977+9Ee+/vWTvv71R77+9Yu+/vT4S77+977+9V++/vT/vv70+Lu+/ve+/vTgj77+977+9cVEXPXAR77+9L++/vVDvv73vv71h77+9eu+/vdWh77+977+92YcD77+9H++/ve+/vceD77+9DERJ77+9dO+/vdum77+9dhYI77+977+9b++/vTnvv73vv73vv73vv73vv716cH3vv71CfTXvv73vv71sFHvvv73vv70G77+9OO+/ve+/ve+/ve+/vcib77+977+977+977+9Be+/vXViJu+/vUnvv73Iie+/vTRNMu+/ve+/vVsZe/OnmoFSKlFBEiIR77+977+9GCfvv71MEO+/vRnvv71JPu+/vUVE77+9S0hz77+9Yi/vv71lFBfvv73vv73vv71tUXnvv70q77+9f++/vXhTRUBV77+9Kz3QoHHvv73vv70sczXvv73vv73vv73vv73vv71k77+9RmHvv71rLO+/vVTvv716P2l477+9QUd9Gu+/vSHvv71m77+9TzofO++/vUvvv70i77+977+9J3wd77+9yZl4Tk/vv73vv70O77+977+977+9ay4a77+9B++/vV4j77+977+977+977+9F28qThjvv71T77+977+977+9Q++/vVrvv73vv73vv70LDxJZQwPvv70PdO+/ve+/ve+/vWIoLS3vv73vv70V77+9YnHvv71s77+977+9JjHvv70k0p7vv70zeu+/vQXvv73vv73vv70d77+9NVhh77+977+977+9UO+/vRYb77+9Y++/vV1r77+9PR4/AO+/ve+/vXFoM++/ve+/ve+/ve+/ve+/vRpA77+977+977+9z7tHWu+/vRld77+9TO+/vRHvv73vv70Pbxvvv73vv71mbyEPR++/ve+/vW/FvX1977+9V2Pvv71vyovvv70iVxLXo++/ve+/vUHvv73vv71XFu+/vSzvv73vv73vv71R77+977+9C3oC77+977+977+9XwplbmRzdHJlYW0KZW5kb2JqCjEgMCBvYmoKPDwgL0NyZWF0aW9uRGF0ZSAoRDoyMDIxMTIxNjE0MzI1N1opIC9DcmVhdG9yIChUZVgpIC9Nb2REYXRlIChEOjIwMjExMjE2MTQzMjU3WikgL1BURVguRnVsbGJhbm5lciAoVGhpcyBpcyBwZGZUZVgsIFZlcnNpb24gMy4xNDE1OTI2NTMtMi42LTEuNDAuMjMgXChUZVggTGl2ZSAyMDIxXCkga3BhdGhzZWEgdmVyc2lvbiA2LjMuMykgL1Byb2R1Y2VyIChwZGZUZVgtMS40MC4yMykgL1RyYXBwZWQgL0ZhbHNlID4+CmVuZG9iagoyIDAgb2JqCjw8IC9UeXBlIC9YUmVmIC9MZW5ndGggMjEgL0ZpbHRlciAvRmxhdGVEZWNvZGUgL0RlY29kZVBhcm1zIDw8IC9Db2x1bW5zIDQgL1ByZWRpY3RvciAxMiA+PiAvVyBbIDEgMiAxIF0gL1NpemUgMyAvSUQgWzw0ZGFjMTgxZWIxMGU1NjljYjc5MzBhYmQzYmJkMzZlMT48ZjhmNGE2YjlmNzU2MmEzMzMzNzI2MTQzNjc5NjMxNDA+XSA+PgpzdHJlYW0KeO+/vWNiAAImRu+/vV4GJgbvv71fDAAH77+9Ae+/vQplbmRzdHJlYW0KZW5kb2JqCiAgICAgICAgICAgICAgIApzdGFydHhyZWYKMjE2CiUlRU9GCg==",
            "status_code": 200,
        }
        self.assertEqual(actual, expected)

    @patch("six.moves.urllib.request.urlopen", side_effect=Util.mocked_request)
    def test_get_txt_file(self, mock_get):
        actual = self.action.run({Input.URL: "https://test.com/v1/test.txt", Input.IS_VERIFY: False})
        expected = {
            "bytes": "dGVzdAp0ZXN0IGZpbGUKc29tZSB0ZXN0IGRhdGE=",
            "status_code": 200,
        }
        self.assertEqual(actual, expected)

    @patch("six.moves.urllib.request.urlopen", side_effect=Util.mocked_request)
    def test_get_txt_file_with_checksum(self, mock_get):
        actual = self.action.run(
            {
                Input.URL: "https://test.com/v1/test.txt",
                Input.CHECKSUM: "5084335576ea9ec4e9d1dcd7536dec3713b3a57a",
                Input.IS_VERIFY: False,
            }
        )
        expected = {
            "bytes": "dGVzdAp0ZXN0IGZpbGUKc29tZSB0ZXN0IGRhdGE=",
            "status_code": 200,
        }
        self.assertEqual(actual, expected)

    @patch("six.moves.urllib.request.urlopen", side_effect=Util.mocked_request)
    def test_get_txt_file_with_bad_checksum(self, mock_get):
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.URL: "https://test.com/v1/test.txt",
                    Input.CHECKSUM: "5084335576ea9ec4e9d1dcd7536dec3713b3a57aa",
                    Input.IS_VERIFY: False,
                }
            )

        self.assertTrue("GetURL Failed" in context.exception.cause)
        self.assertTrue(
            "Any of file checksums {'md5': '3f290592253742c1ffeac7ccf5d678fd', 'sha1': '5084335576ea9ec4e9d1dcd7536dec3713b3a57a', 'sha256': '231023899ac36cad7fd0c6f034e5ac7c6d0f1ad40400c7e970ed984f8d49cc9b', 'sha512': '51548730d6fda0ab56e43be0b2a943fd808632bd9decc05e46a6e95531940da4b0274a5ab1c8176ca994591ab38105d9de5161b214bd5a4ef2844f005ea0da5a'} does not match 5084335576ea9ec4e9d1dcd7536dec3713b3a57aa."
            in context.exception.assistance
        )

    @patch("komand.helper.open_url", side_effect=Util.mocked_url_open)
    def test_is_verify(self, mock_get):
        actual = self.action.run({Input.URL: "https://test.com/v1/test.txt", Input.IS_VERIFY: True})
        self.assertTrue(mock_get.call_args_list[0][1].get("verify"))
