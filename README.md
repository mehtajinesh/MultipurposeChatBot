## How to use this repo

The code of this repo differs quite significantly from the original video. This is how to use it:

### Training the NLU model

Since the release of Rasa 1.0, the training of the NLU models became a lot easier with the new CLI. Train the model by running:  

```rasa train nlu ```

Once the model is trained, test the model:

```rasa shell nlu```


### Training the dialogue model

The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` rasa run actions```  

2. Open a new terminal and train the Rasa Core model by running:  

``` rasa train```  

3. Talk to the chatbot once it's loaded after running:  
```rasa shell```  


### Starting the interactive training session:

To run your assistant in a interactive learning session, run:
1. Make sure the custom actions server is running:  

```rasa run actions```  

2. Start the interactive training session by running:  

```rasa interactive```  

Latest code update: 02/01/2020

Latest compatible Rasa NLU version: 1.16
