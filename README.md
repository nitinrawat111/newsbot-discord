# newsbot-discord
A discord bot which fetches news from multiple sources. It is build using dicord.py API wrapper for Discord. It uses NewsAPI to fetch the required news headlines.

## Running the bot on Replit
1. Import the repository on <a href = "https://replit.com/">Replit</a>. No need to install dependencies as replit will do it automatically when you execute the bot.

2. Create a new application on <a href = "https://discord.com/developers/applications">Discord Developer Portal</a> and afterwards create a bot on the portal.

3. Generate the invite url for the bot and make sure to give it the following permissions:
    - Send Messages
    - Send Messages in thread
    - Embed Links

4. Add the bot to your server by visiting the generated url and selecting the desired server.

5. Copy the API Token for your bot and place it in the repl.it environment variable as 'TOKEN'.

6. Now, generate the API key for <a href = "https://newsapi.org/">NewsAPI</a>. Add the API key to the repl.it environment vairables as 'NEWSAPIKEY'.

7. Now just execute the main.py file in the repl.

8. As long as it is running, the bot will be online and will respond to commands.

## Running the bot on native environment
1. Install the dependencies.
    - <a href = "https://discordpy.readthedocs.io/en/stable/intro.html">discord.py</a>
    - <a href = "https://github.com/mattlisiv/newsapi-python">NewsAPI Pyhton Library</a>

2. Clone the repository.

3. Create a new application on <a href = "https://discord.com/developers/applications">Discord Developer Portal</a> and afterwards create a bot on the portal.

4. Generate the invite url for the bot and make sure to give it the following permissions:
    - Send Messages
    - Send Messages in thread
    - Embed Links

5. Add the bot to your server by visiting the generated url and selecting the desired server.

6. Copy the API Token for your bot. Replace the 'TOKEN' on the last line of main.py with the copied token(enclosed in quotes).

7. Now, generate the API key for <a href = "https://newsapi.org/">NewsAPI</a>. Replace 'NEWSAPIKEY' in main.py with this copied key.

8. Now just execute the main.py file:
    ```
    pyhton main.py
    ```

9. As long as it is running, the bot will be online and will respond to commands.

## Usage
|           Commands               |                Description                                               |
|----------------------------------|--------------------------------------------------------------------------|
|            $top                  | Displays top 5 headlines in the text channel.                            |
|            $q <query>            | Searches for news articles with "query". It can be of multiple words.<br>Advanced Search is also supported.<br> - Surround phrases with quotes (") for exact match.<br>- Prepend words or phrases that must appear with a + symbol.<br>- Prepend words that must not appear with a - symbol.<br>- You can use the AND / OR / NOT keywords.|
|            $tops                 | Same as $top but it does not send links along with headlines. Useful when you want to reduce clutter due to link preview.|
|            $qs <query>           | Same as $q <query> but it does not send links along with headlines. |
                                      

## Contributions and Support
Feel free to improve the code further by optimizing, adding new features, improving readability or any other changes. Any suggestions and feedback will be much appreciated.
