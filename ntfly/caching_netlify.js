/*
input: csv file
method:
    - descriptively: find common packages used across the 100 builds
        * frequency of package occurrence (ex: @gatsbyjs/reach-router )
            - constraint: 100 builds
                - find packages that occur in at least 100 builds
                    * provide counter for builds found that have such counts
                    * take into account size
        * data allocation of each package (refer to repo that has package size)
            - await, fetch -> npm registry, package phobia
                * data of each size of package
    - actual method:
        # confirmed build that is used in at least 100 builds
        # sorted in order of frequency
        [
        # highest frequent package
        {
            "package":"bootstrap",
            "size": "5mb",
            "frequency": "1000"
        },
        ...
        {
        "package": "astrojs",
        "size":"100mb",
        "frequency":"100"
        }
output:
    - descriptively: quantity of disk space saved if we cached packages used across 100 builds
*/

const fs = require('fs');
const csvText = fs.readFileSync('builds-packages.csv', 'utf8');
const csv_file = csvText.trim().split('\n').slice(0, 1000) // Array of row

function cache_savior(input_file) {

    // gets package frequency
    const package_list_dict = []
    while (package_list_dict.length < 10) {
        // loop over csv file,....
        for (let i = 0; i < input_file.length; i++) {

            // filter through csv for package and it's name
            let package_arr = input_file[i].split(",")
            let package_name = package_arr[1]

            //iterate over current package dicts and ask if dict with package name is currently in it
            let packageFound = false

            if (package_list_dict.length === 0) {
                package_list_dict.push({
                    package: package_name,
                    frequency: 1
                })
            }

            // now we are sure we have at least 1 element so we need

            package_list_dict.map((package_dict) => {
                // check against if it's currently in dict, if in dict increment
                package_list_dict.forEach((package_dict) => {
                    if (package_dict.package === package_name) {
                        if (package_dict.frequency < 100) {
                            package_dict.frequency += 1;
                            packageFound = true
                        }
                    }
                })
                // if it's not in dict create a new allocation for it
                if (!packageFound) {
                    package_list_dict.push({
                        package: package_name,
                        frequency: 1
                    })
                }
            })
            if (package_list_dict.length === 100) {
                break
            }
        }

        package_list_dict.sort((a, b) => b.frequency - a.frequency);
        const filtered_list = package_list_dict.filter(dict => dict.frequency >= 100).slice(0, 10);

        async function get_package(filtered_list) {
            // we want to get the size using the npm directory
            for (let dict of filtered_list) {
                const response = await fetch(`https://registry.npmjs.org/${dict.package}`)
                if (!response.ok) {
                    console.log('not ok')
                }
                if (response.ok) {
                    let data = await response.json()
                    let latest = data['dist-tags'].latest;
                    let unpackedSize = data.versions[latest].dist.unpackedSize;
                    dict['size_mb'] = unpackedSize / (1024 ** 2)
                }

            }
            return filtered_list
        }
        (async () => {
            const result = await get_package(filtered_list)
            console.log(result)

            const sum = result.reduce((acc, dict) => {
                return acc + (typeof dict.size_mb === 'number' ? dict.size_mb : 0);

            }, 0)
            console.log(`this is the saved ${sum}`)
        })();
    }
}


cache_savior(csv_file)
console.log
