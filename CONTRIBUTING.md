# Cómo contribuir a este proyecto

## Flujo de ramas
Nunca se trabaja directamente sobre `main`. Para cada cambio se crea una
rama nueva a partir de `main` (`git switch -c nombre-descriptivo`).

## Mensajes de commit
Se sigue el formato `tipo: descripción`, con los tipos `feat`, `fix`,
`docs`, `style`, `refactor`, `test` y `chore` (ya usados en la práctica
de Git en local).

## Cómo proponer un cambio
1. Crea una rama desde `main`.
2. Sube tus commits en ella.
3. Sube la rama: `git push -u origin nombre-de-la-rama`.
4. Cuando hayas terminado, abre una Pull Request en GitHub describiendo el cambio.
5. Espera la revisión antes de fusionar.

## Cómo clonar y ejecutar este proyecto
git clone git@github.com:Jesus10011/ut2-git-python.git
cd ut2-git-python
python3 ej01_par_impar.py
