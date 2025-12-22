function largest_subarray_k_sum(
    input_array,
    K
) {
    if (
        input_array.length === 0
    ) {
        return 0
    }

    let globalMax = input_array[0]
    let currentMax = input_array[0]

    for (
        let i = 0; i < input_array.length; i++
    ) {
        currentMax = Math.max(
            input_array[i],
            currentMax + input_array[i]
        )
        if(currentMax > globalMax){
            globalMax = currentMax
        }
    }
}
