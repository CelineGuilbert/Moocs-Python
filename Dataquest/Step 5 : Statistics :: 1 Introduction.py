# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response)
 for response in survey_responses] #retourne : [0, 2, 3, 0, 1, 0, 0]
average_smoking = sum(survey_numbers) / len(survey_numbers)  
    
