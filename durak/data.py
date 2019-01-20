SUITES = 'H D S C'.split()
RANKS = '6 7 8 9 10 V Q K A'.split()
RANK_NR = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'V': 11, 'Q': 12, 'K': 13, 'A': 14}

TITLE = '''
***********************************************

    * *     *     * ****        ***     *   *
    *   *   *     * *   *      *   *    *  *
    *    *  *     * * *       *     *   **
    *   *   *     * *   *    * ***** *  * *
    ***      ****   *    *  *         * *   *

***********************************************
 '''

RULES = '''
    1. Kiekvienam zaidejui isdalijama po 6 kortas.
    2. Paskutine korta atverciama, ji bus koziriu.
    3. Pradeda tas, kuris turi maziausia koziri arba is vis jo neturi.
    4. Zaidziama pagal laikrodzio rodykle.
    5. Korta kerta didesne tos pacios mosties korta arba koziris.
    6. Visos atmustos kortos dedamos i sali.
    7. Jei zaidejas nebeturi didesnes kortos arba kzoirio pasiima padeta korta.
    8. Kai bent vienas is zaideju bebeturi kortu pasiima is kortu kalakdes tiek,
       kad kiekvienas turetu po 6 kortas.
    9. Zaidima pralaimi susirinkes kortas, o laimi tas zaidejas, kuris isleidzia
       visas kortas.

 '''
CARDS = { 'H 6': '''  --------------
                     |   *** ***    |
                     |  *   *   *   |
                     |    *   *     |
                     |      *       |
                     |      6       |
                      --------------
                ''' ,
          'H 7': '''  --------------
                     |   *** ***    |
                     |  *   *   *   |
                     |    *   *     |
                     |      *       |
                     |      7       |
                      --------------
                ''' ,
           'H 8': '''  --------------
                      |   *** ***    |
                      |  *   *   *   |
                      |    *   *     |
                      |      *       |
                      |      8       |
                       --------------
                 ''' ,
           'H 9': '''  --------------
                      |   *** ***    |
                      |  *   *   *   |
                      |    *   *     |
                      |      *       |
                      |      9       |
                       --------------
                   ''' ,
         'H 10': ''' --------------
                    |   *** ***    |
                    |  *   *   *   |
                    |    *   *     |
                    |      *       |
                    |      10      |
                     --------------
               ''' ,

}
