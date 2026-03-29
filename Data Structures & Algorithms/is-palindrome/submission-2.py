class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Inicializamos dos punteros:
        # l apunta al inicio, r al final del string
        l, r = 0, len(s) - 1

        # Recorremos mientras los punteros no se crucen
        while l < r:

            # Avanzamos el puntero izquierdo hasta encontrar un carácter alfanumérico
            # (ignoramos espacios, símbolos, etc.)
            while l < r and not s[l].isalnum():
                l += 1

            # Retrocedemos el puntero derecho hasta encontrar un carácter alfanumérico
            while l < r and not s[r].isalnum():
                r -= 1

            # Comparamos ambos caracteres en minúscula para evitar problemas de mayúsculas
            if s[l].lower() != s[r].lower():
                # Si no coinciden, no es palíndromo
                return False

            # Si coinciden, avanzamos ambos punteros hacia el centro
            l += 1
            r -= 1

        # Si nunca encontramos diferencias, es palíndromo
        return True