Select p_client.idClient as 'ID клиента', Client_Name, Birthday, MilesBalance, Date_Balance, COUNT(*) AS Total
FROM ticket INNER JOIN p_client ON p_client.idClient=ticket.idClient
WHERE YEAR(Buy_Date)='$year' AND month(Buy_Date) between '$month1' and '$month2'
GROUP BY ticket.idClient order by Total DESC
limit $num