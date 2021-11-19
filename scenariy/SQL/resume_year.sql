select A_out, month(Flight_Date), Class, count(Class) as Col
from b_miles.ticket join b_miles.flight on ticket.Flight_number = flight.Flight_Number
where year(Flight_Date)='$year'
group by Class, A_out