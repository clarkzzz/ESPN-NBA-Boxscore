# ESPN-NBA-Boxscore
This is a simple web crawling project that I have made.
The purpose of the script is to obtain NBA players' boxscore data once the script is provided with an ESPN webpage.

The key components in the scripts:
- Extract the <tr> tags
- Retain <tr> tags that are relevant to players
- Convert to dataframe
- Fill NaN to players who are DNP (Did Not Play)
  
## Future revisions:
- Parse player id (as different players may share the same name)
- Autocrawl game id
- Export to csv
