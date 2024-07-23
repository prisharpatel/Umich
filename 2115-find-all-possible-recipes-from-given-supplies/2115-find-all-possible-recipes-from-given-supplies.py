class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        # need to return a list of recipes that u can create iwth the ingredients and supplies that you have 
        # ingredients could be other recipes or raw materials
        # supplies are just raw materials and you have unlimited supplies of them

        # graph --> dfs --> start at recipes --> go to ingredients --> go to supplies?
        # bfs - use a queue - not tracking a pathway 
        # 

        # pseudocode: 
        # make a hash for recipe --> index
        # q = deque([recipes])
        # originalLen = len(recipes) # need to store this value because we are addign on to a queue after going through the original recipes
        # createdRecipes = set()  == for O(1) access
            # while loop for recipes: 
                # bool make = false
                # for j in  ingredients[i]: 
                    # see if j is in supplies: 
                        # continue
                    # see if j is in recipes
                        # continue
                    # add to queue other wise and set to false
        
        recipeIndex = {}
        for i, recipe in enumerate(recipes):
            recipeIndex[recipe] = i
        
        q = deque(recipes)
        n = len(recipes)
        createdRecipes = set()
        while q: 
            make = True
            recipe = q.popleft()
            i = recipeIndex[recipe]
            for j in ingredients[i]:
                if j in supplies:
                    continue
                if j in createdRecipes:
                    continue
                if j in recipes:
                    # add to queue
                    make = False 
                    q.append(recipe)
                    continue
            if make:
                createdRecipes.add(recipe)

        return list(createdRecipes)

                    
        