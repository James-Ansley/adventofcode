fun read(path: String): String =
    object {}.javaClass.getResource(path)!!.readText().trimEnd()


fun readLines(path: String): List<String> =
    read(path).lines()


fun readInts(path: String): List<Int> =
    read(path).lines().map { it.toInt() }


fun <T> List<List<T>>.transpose(): List<List<T>> =
    this[0].indices.map { j -> this.indices.map { i -> this[i][j] } }