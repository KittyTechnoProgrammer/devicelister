# HoleScan

HoleScan is a project to help with metasploit vulneriablity scanning. HoleScan has two scanning modes. The first is Metasploit
Mode (MM). Metasploit Mode will use nmap to scan a target, detect only OPEN ports (you can change this but not advised). Detect
those open ports protocol and target OS (Attempt to anyway). Then using that information find exploits in your local metasploit
exploit modules, and run a check on each on (Some don't support check). Then save these results into a database in metasploit
(if you chose to).

## Getting Started

To get started run "sudo pip3 install -r requirments.txt".
You also need to make a shodan account.

### Prerequisites

Python3
Shodan Python3 module
Shodan account


### Installing

All you need to do is run "sudo pip3 install -r requirments.txt"

## Running the tests

To test this you can run "./devicelister.py -k shodankey -q routers -o routerlist.txt"
This should produce a list of routers. However, please know that some queries can break shodan.

If your experience problems let me know.

### Break down into end to end tests

That test should make sure that everything is installed and running correctly.


## Deployment

This can be used when trying to make a list of large of devices that match your query.

## Built With

Python3, Shodan python3 module, and common sense.

## Contributing

Right now just me KittyTechnoProgrammer

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Brandon Armstrong**

See also the list of [contributors](JustMe) who participated in this project.

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used

    Creaters of Shodan and Shodan API

* Inspiration

    Target list creation.

* etc

    If you would like to add any featurs that I am not aware of. Please contact me at kittytechno@protonmail.com