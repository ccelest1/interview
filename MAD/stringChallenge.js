/**
 * @param {string} input_str
 * @returns {Array[string]}
 */
function stringChallenge(input_str) {

    let float_str = parseFloat(input_str)
    let visual_stars = 0

    const StarHelper = (round_stars, visual_stars) => {
        if (!round_stars || round_stars < .25) {
            return visual_stars
        }
        return StarHelper(round_stars - .5, visual_stars + .5)
    }

    const stars = StarHelper(float_str, visual_stars)

    /**
     *
     * @param {Number} stars
     * @param {Array[]} res
     * @param {Array[string]} res
     */
    const return_visual_stars = (stars, res = []) => {
        while (stars > .25) {
            if (stars > .5) {
                res.push('full')
                stars -= 1
            } else {
                res.push('half')
                stars -= .5
            }
        }
        while (res.length < 5) {
            res.push('empty')
        }
        return res.join(' ')
    }
    return return_visual_stars(stars)

}

const inputs = [
    JSON.stringify(stringChallenge(2.5)),
    JSON.stringify(stringChallenge(4.9)),
    JSON.stringify(stringChallenge(.4))

]

const checks = [
    JSON.stringify('full full half empty empty'),
    JSON.stringify('full full full full full'),
    JSON.stringify('half empty empty empty empty')
]

for (let i = 0; i < inputs.length; i++) {
    if (inputs[i] === checks[i]) {
        console.log(true)
    } else {
        console.log(inputs[i])
        console.log(false)
    }
}
