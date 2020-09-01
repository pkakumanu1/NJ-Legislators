db_user = 'postgres'
db_pswd ='Padmini1!'

mayor_query = 'select Distinct "Mayor_Name", "eMail", "Address", "Phone","Term_End" from "NJLSchema"."MunicipalMayors" where "Town" in (' +"{}" + ')'

senator_query ='select Distinct "Name","Address" from "NJLSchema"."Senators" as s,"NJLSchema"."Senatoraddress"as sa, "NJLSchema"."Dist_Municipality" as dm where s."Dist_Id" = sa."Dist_Id" and s."Dist_Id" = dm."Dist_Id"and "Town" in ('+"{}"+')'

assembly_query = 'select Distinct "Name","Address" from "NJLSchema"."Assembly" as a,"NJLSchema"."AssemblyPersonAddress" as aa,"NJLSchema"."Dist_Municipality" as dm where a."Dist_Id"=aa."Dist_Id" and a."Dist_Id"=dm."Dist_Id" and "Town" in (' + "{}" +')'