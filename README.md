**ЗАДАНИЕ**

Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
  - getAll() Должен возвращать изначальный массив элементов.
  - getItem(id) Принимает id элемента и возвращает сам объект элемента;
  - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
 чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
  - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
 начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
 т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!
