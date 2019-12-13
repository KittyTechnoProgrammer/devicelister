#!/usr/bin/env python3

# <devicelister is a tool for querying shodan and making a list of IP's matching that>
#     Copyright (C) 2019  Brandon Armstrong

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# <devicelister>  Copyright (C) <2019>  <Brandon Armstrong>
#     This program comes with ABSOLUTELY NO WARRANTY. I am not responsible for any damage
#     that may be caused by the use of this tool.
#     This is free software, and you are welcome to redistribute it
#     under certain conditions. Those conditions being that I am also given credit.

import shodan
 import sys
from argparse import ArgumentParser

def getArgs() :

    parser = ArgumentParser()
    parser.add_argument("-q",dest="query", help="Set the query to search for in shodan")
    parser.add_argument("-query",dest="query", help="Set the query to search for in shodan")
    parser.add_argument("-o", dest="output", help="Set the output file")
    parser.add_argument("--out", dest="output", help="Set the output file")
    parser.add_argument("-k", dest="key", help="Set the Shodan Key")
    parser.add_argument("--key", dest="key", help="Set the Shodan Key")
    parser.add_argument("--version", dest="version", action="store_true", help="Show the version of devicelister")


    args = parser.parse_args()

    if args.version :

        print("devicelister Version : 1.0.0")
        sys.exit(0)

    if not args.key :

        print("Need a query for shodan")
        print("Example : ./devicelister.py -k shodankey -q yourquery -o filename")
        print("Use -h for more help")
        sys.exit(1)

    if not args.query :

        print("Need a query for shodan")
        print("Example : ./devicelister.py -k shodankey -q yourquery -o filename")
        print("Use -h for more help")
        sys.exit(1)

    if not args.output :

        print("Warning No Output file specified. Will NOT SAVE IN FILE!!!")
        # print("Need a output for shodan")
        # print("Example : ./devicelister.py -q yourquery -o outputfile")
        print("Use -h for more help")

    return args


def main() :

    args = getArgs()

    shodan_api_key = args.key
    api = shodan.Shodan(shodan_api_key)

    try :
        #print(len(sys.argv))

        print("Searching For : {}".format(args.query))
        results = api.search("{}".format(args.query))
        print("Result Found : {}".format(results['total']))

        if args.output :

            fout = open("{}".format(args.output) , "w")

        matches = []
        for result in results['matches'] :

            if result['ip_str'] not in matches :

                matches.append(result['ip_str'])
                print("IP : {}".format(result['ip_str']))
                #print("{}".format(result['data']))
                if args.output :

                    fout.write("{}\n".format(result['ip_str']))

        if not args.output :

            print("Warning No Output file specified. Will NOT SAVE IN FILE!!!")

    except shodan.APIError as err :

        print(err)
        if "The search request timed out" in err:

            print("Try searching in your browser, and see what you get!!")
            print("Some queries can break shodan")

        elif "your query was invalid" in err :

            print("Try searching in your browser, and see what you get!!")
            print("Some queries can break shodan")

        sys.exit(1)

if __name__ == "__main__" :

    main()
