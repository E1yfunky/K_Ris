Select p_client.idClient, Client_Name, Birthday, MilesBalance, Date_Balance
FROM b_miles.p_client LEFT JOIN b_miles.ticket ON p_client.idClient=ticket.idClient
WHERE ticket.Ticket_Number is NULL