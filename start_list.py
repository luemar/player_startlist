def start_list(all_players, num_in_flight, num_day_played):
    """For 16 golf players playing in flights/groups of 4, on 5 or 4 or 3 days/occations,
    create startlists with eyery player playing another only once. Fuction to be
    used only with 16-4-5, 16-4-4, 16-4-3."""
    
    print('...............day_1................')
    history = {'a':[], 'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],\
              'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[]}
    
    for lead_player_index in range(0, len(all_players), num_in_flight):
        """Create the first 4 flights alphabetically.""" 
        players = all_players[lead_player_index: lead_player_index + num_in_flight]
        [history[pl_day_1].extend(players) for pl_day_1 in players]
        print(all_players[lead_player_index] + '_flight_day_1:',players)

    for i in range(num_days_played - 1):
        """For each of day 2 to 5 create 4 flights with fixed leading players a, b, c, d."""    
        flights = {}
        c_all_players = all_players[:]
        print('...............day_' + str(i)+'................')
        flights['a_flight_day_'+str(i+2)]= []
        flights['b_flight_day_'+str(i+2)]= []
        flights['c_flight_day_'+str(i+2)]= []
        flights['d_flight_day_'+str(i+2)]= []            
        lead = list('abcd')                   
        flight_list = [flights['a_flight_day_'+str(i+2)], flights['b_flight_day_'+str(i+2)],\
                       flights['c_flight_day_'+str(i+2)], flights['d_flight_day_'+str(i+2)]]

        for j in range(len(flight_list)):            
            def flight(cond, day):
                """Draw 4 players for each flight."""
                for player in all_players:
                    #Select player not in lead player's history, and not in previous flight.
                    if player not in cond:  #Add player to flight.
                        day.extend(player) #Update conditions by player's history.
                        cond.extend(history[player])  #Update lead player's history by selected player.
                        history[lead[j]].extend(player) #Add lead player to flight.
                day.extend(lead[j])
                day.sort()
                [history[pl_day_2_5].extend(day) for pl_day_2_5 in day[1:]]
                """ Update each flightplayer's history by other's history."""
                return lead[j]+'_flight_day_'+str(i+2)+ ': ' + str(flight_list[j])
               
            conditions = [history[lead[j]], history[lead[j]] + flights['a_flight_day_'+str(i+2)],\
                          history[lead[j]] + flights['a_flight_day_'+str(i+2)] + \
                          flights['b_flight_day_'+str(i+2)], \
                          history[lead[j]] + flights['a_flight_day_'+str(i+2)] + \
                          flights['b_flight_day_'+str(i+2)]+ flights['c_flight_day_'+str(i+2)]] 
            print(flight(list(set(conditions[j])), flight_list[j]))

num_in_flight = 4
num_days_played = 5
all_players = list('abcdefghijklmnop')
start_list(all_players, num_in_flight , num_days_played)





    
  
