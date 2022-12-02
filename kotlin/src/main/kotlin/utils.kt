fun read(path: String): String =
    object {}.javaClass.getResource(path)!!.readText().trim()


fun readLines(path: String): List<String> =
    read(path).lines()


fun readInts(path: String): List<Int> =
    read(path).lines().map { it.toInt() }
