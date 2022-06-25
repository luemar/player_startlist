def startlist(all_players, num_in_flight):
    """For 16 players playing in groups/flights of 4,  5 times or on 5 days,
    create startlists with eyery player playing another only once."""
    c_all_players = all_players[:] # copy to be changed
    history = {'a':[], 'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],\
               'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[]}
    print('...............day_1................')
    def day_1_flights():
        """Create the first 4 flights alphabetically."""       
        key_hist = list(history.keys())
        c_key_hist = key_hist[:]
        for dummy_i in c_key_hist:
            print('flights_day_1: ', c_key_hist[:num_in_flight])
            for key in c_key_hist[:num_in_flight]:
                [history[key].append(player)for player in c_all_players[0:num_in_flight]]
            del c_key_hist[:num_in_flight]
            del c_all_players[0:num_in_flight]
    day_1_flights()
    
    def day_2_to_5_flights():
        """For day 2 to day 5 create the 4 flights with fixed leading players
        a, b, c, d."""      
        flights = {}
        for i in range(2,6):
            #Define the 4 flights by their leading players as dict keys
            #for day 2 to day 5.
            print('...............day_' + str(i)+'................')
            flights['a_flight_day_'+str(i)]= []
            flights['b_flight_day_'+str(i)]= []
            flights['c_flight_day_'+str(i)]= []
            flights['d_flight_day_'+str(i)]= []            
            lead = list('abcd')                   
            flight_list = [flights['a_flight_day_'+str(i)], flights['b_flight_day_'+str(i)],\
                           flights['c_flight_day_'+str(i)], flights['d_flight_day_'+str(i)]]

            for j in range(len(flight_list)):            
                def flight(cond, day):
                    """Draw 4 players for each flight."""
                    for player in all_players:
                        #Select player not in lead player's history
                        #and not in previous flight.
                        if player not in cond:
                            #Add player to flight.
                            day.extend(player)
                            #Update conditions by player's history.
                            cond.extend(history[player])
                            #Update lead player's history by selected player.
                            history[lead[j]].extend(player)
                    #Add lead player to flight.
                    day.extend(lead[j])
                    day.sort()
                    #Update each flightplayer's history by other's history.
                    [history[pl].extend(day) for pl in day[1:]]
                    return lead[j]+'_flight_day_'+str(i)+ ': ' + str(flight_list[j])
                   
                conditions = [history[lead[j]], history[lead[j]] + flights['a_flight_day_'+str(i)],\
                              history[lead[j]] + flights['a_flight_day_'+str(i)] + \
                              flights['b_flight_day_'+str(i)], \
                              history[lead[j]] + flights['a_flight_day_'+str(i)] + \
                              flights['b_flight_day_'+str(i)]+ flights['c_flight_day_'+str(i)]] 
                print(flight(list(set(conditions[j])), flight_list[j]))
    day_2_to_5_flights()
startlist(list('abcdefghijklmnop'), 4)
