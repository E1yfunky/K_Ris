Select  p_client.idClient, Client_Name, Birthday, MilesBalance, Date_Balance
FROM b_miles.p_client
WHERE NOT exists (Select ticket.idClient FROM b_miles.ticket
WHERE YEAR(Buy_Date)='$year' AND MONTH(Buy_Date)='$month' AND ticket.idClient=p_client.idClient)