export async function fetchQuestions(amount, difficulty) {
    const params = new URLSearchParams({ amount, difficulty })
    const url = `https://opentdb.com/api.php?${params}`
    const res = await fetch(url)
    if (!res.ok) {
        throw new Error(`Network error: ${res.status}`)
    }
    const data = await res.json()

    return data.results
}