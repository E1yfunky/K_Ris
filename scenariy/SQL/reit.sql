Select p_client.idClient, Client_Name, Birthday, MilesBalance, Date_Balance
FROM b_miles.p_client JOIN b_miles.ticket ON p_client.idClient=ticket.idClient
WHERE Flight_number='$r_num' AND Cost=(Select MAX(Cost) FROM ticket WHERE Flight_number='$r_num')