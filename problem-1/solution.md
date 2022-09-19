<!-- TODO -->
POST /catfacts
{
"breed" : "persian",
"fact" : "It is a long-haired breed of cat characterized by a round face and short muzzle."
} //특정 품종 등록

PATCH /catfacts/1
{
"fact" : "It is a long-haired breed of cat characterized by a round face and short muzzle. The first documented ancestors of Persian cats were imported into Italy from Persia around 1620."
} //특정 품종 수정

DELETE /catfacts/1
