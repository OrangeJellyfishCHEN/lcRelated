class LC735(object):
    def asteroidCollision(self, asteroids):
        ast_stack = []
        for ast in asteroids:
            ast_alive = True
            while ast_alive and ast < 0 and len(ast_stack) > 0 and ast_stack[-1] > 0:
                ast_alive = ast_stack[-1] < -ast
                if ast_stack[-1] <= -ast:
                    ast_stack.pop()
            if ast_alive:
                ast_stack.append(ast)
        return ast_stack