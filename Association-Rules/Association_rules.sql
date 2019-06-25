
/**********************************************************************************************/
   /*
   * nomenclature FRANCE 
   * RESTRICTION PERIMETRE : ne conserver que les produits identifiés dans la nomenclature DPC 
   * ne pas se baser sur la nomenclature FRANCE
   * 72 895 produits
   */ 
/**********************************************************************************************/

drop table nomenclature_;
create volatile table nomenclature_
(
prd_item_unique_code  character(13),
nomenclature_lvl1_sde varchar(200),
nomenclature_lvl2_sde varchar(200),
nomenclature_lvl3_sde varchar(200),
nomenclature_lvl4_sde varchar(200),
prd_sku_sde varchar(200),
BRAND_SECONDARY varchar(200),
top_ownbrand integer,
dte_ean_h date,
sid_sku_h integer
)
primary index(prd_item_unique_code)
ON COMMIT PRESERVE ROWS;

INSERT INTO  nomenclature_
SELECT 
	EAN.prd_item_unique_code, 
	REF.nomenclature_lvl1_sde, REF.nomenclature_lvl2_sde, REF.nomenclature_lvl3_sde, REF.nomenclature_lvl4_sde,
	REF.prd_sku_sde, REF.BRAND_SECONDARY , case when REF.BRAND_SECONDARY like '%COSMIA%' then 1 else 0 end as top_ownbrand,
	dte_ean_h, sid_sku_h
FROM  /* liaison table produit Côté France, Filtre sur le DEPARTMENT */
	(select sid_sku_h, id_code_ean_h, id_key_ean_h, (id_code_ean_h||id_key_ean_h) as prd_item_unique_code, dte_ean_h
	 from FRDM_BEO_V.LU_EAN_H where sid_department_h in (163,246) and dte_ean_h >='2018-01-01' ) as EAN  
	/* ne conserver que les articles du référentiel catmans */
INNER JOIN FRDM_SPSS.referentiel_marque  as REF 
	on REF.prd_item_unique_code=EAN.prd_item_unique_code
	/* nomenclature où présence d'une référence en MDDI */
;


/**********************************************************************************************/		
/* supp les doublons de sku !! utile pour la liaison aux ventes !!  */
/**********************************************************************************************/
		
drop table nomenclature;		
create volatile table nomenclature
(
prd_item_unique_code  character(13),
nomenclature_lvl1_sde varchar(200),
nomenclature_lvl2_sde varchar(200),
nomenclature_lvl3_sde varchar(200),
nomenclature_lvl4_sde varchar(200),
prd_sku_sde varchar(200),
BRAND_SECONDARY varchar(200),
top_ownbrand integer,
dte_ean_h date,
sid_sku_h integer
)
primary index(prd_item_unique_code)
ON COMMIT PRESERVE ROWS;

INSERT INTO  nomenclature
select *
from nomenclature_
qualify
   row_number() over (partition by sid_sku_h order by dte_ean_h) = 1
;










/*** Modele ASSOCIATION RULES ***/
/*
 *Ticket Noyelles sur 2018
 * Uniquement sphère Beauté
 */
 
drop table tck ;
create volatile table tck (
id_day date,
SID_STORE int,
sid_unique_basket bigint,
sid_customer int,
quantite int,
f_val_sales_total_wt_tck decimal(38,4),
sid_sku_h int,
SID_SUB_DEPARTMENT_H int,
sid_family_h int,
marque_ds varchar(255),
nomenclature_lvl1_sde varchar(200),
nomenclature_lvl2_sde varchar(200),
nomenclature_lvl3_sde varchar(200),
nomenclature_lvl4_sde varchar(200),
prd_sku_sde varchar(200)
)
primary index(sid_sku_h)
ON COMMIT PRESERVE ROWS;




INSERT INTO tck  
SELECT TCK.id_day, TCK.SID_STORE, TCK.sid_unique_basket, tck.sid_customer, tck.quantite, tck.f_val_sales_total_wt_tck, tck.sid_sku_h,
       EAN.SID_SUB_DEPARTMENT_H, EAN.sid_family_h, BRAND.MARQUE_DS,
	   HB.nomenclature_lvl1_sde, HB.nomenclature_lvl2_sde, HB.nomenclature_lvl3_sde, HB.nomenclature_lvl4_sde,
	   HB.prd_sku_sde
FROM (
		select SID_STORE, id_day, sid_unique_basket, sid_customer,  quantite, f_val_sales_total_wt_tck, sid_sku_h
		from FRDM_BEO_V.V_TICKET_DETAIL_NET  
		WHERE ID_DAY>= '2018-01-01' and ID_DAY<= '2018-12-31' and quantite>0 and sid_customer>0
	   ) as TCK
INNER JOIN(  /* liaison table produit Côté France, Filtre sur le DEPARTMENT */
		select sid_sku_h, id_code_ean_h, id_key_ean_h,  dte_ean_h, SID_SUB_DEPARTMENT_H, sid_family_h
	    from FRDM_BEO_V.LU_EAN_H 
	    where sid_department_h in (246) /*and SID_SUB_DEPARTMENT_H=1830*/  and dte_ean_h>= '2018-01-01'
	    ) as EAN  
	 	on EAN.sid_sku_h=TCK.sid_sku_h and ean.dte_ean_h >= tck.id_day
INNER JOIN (
		select * 
		from FRDM_BEO_V.lu_site 
		where id_postal_code in ('62950'/*,'59320'*/)
		) as SITE on TCK.SID_STORE = SITE.SID_SITE 
INNER JOIN (
		select *
		from FRDM_POF.POF_SKU_NAT_IRI_UNIQUE
		) as idBRAND 
		on idBRAND.sid_sku_h=TCK.sid_sku_H
INNER JOIN (
		select *
		from FRDM_SPSS.POF_IRI_MARQUE
		) as BRAND
		on idBRAND.sid_marque=BRAND.sid_marque and BRAND.DTF>=TCK.id_day
LEFT JOIN nomenclature as HB /* nomenclature HB */
		on HB.sid_sku_h=TCK.sid_sku_H
;



/* Table pour input du modèle
 * 
 * Group by Customer 
 */
drop table frdm_spss.tck_CUST;
create  table frdm_spss.tck_CUST (
sid_customer int,
nomenclature_lvl1_sde varchar(200),
nomenclature_lvl2_sde varchar(200),
nomenclature_lvl3_sde varchar(200),
nomenclature_lvl4_sde varchar(200),
prd_sku_sde varchar(200),
marque_ds varchar(255),
product_qty int
)
primary index(sid_customer)
;

insert into frdm_spss.tck_CUST
select sid_customer,  nomenclature_lvl1_sde, nomenclature_lvl2_sde, nomenclature_lvl3_sde, nomenclature_lvl4_sde,  prd_sku_sde , marque_ds, 
sum(quantite) as product_qty
from tck 
group by 1,2,3,4,5,6,7
;

select * from frdm_spss.tck_CUST sample 50 ;




/*** ITALIE ***/

SELECT person_unique_code , 
ds_cst_segmentation, 
nomenclature_lvl4_sde , nomenclature_lvl3_sde , nomenclature_lvl2_sde ,
nomenclature_lvl1_sde , prd_item_unique_code , prd_sku_sde , BRAND_SECONDARY ,
sum(nbr_products) as product_qty
FROM `ard-dataviz-sandbox.COSMIA_032019.cosmia_customer_J`
where ds_cst_segmentation not in ('NEW','PROSPECT','0 STAR','PAS DE CALCUL','NON_CARTE','1 STAR','INACTIVE')
group by 
person_unique_code , 
ds_cst_segmentation, 
nomenclature_lvl4_sde , nomenclature_lvl3_sde , nomenclature_lvl2_sde ,
nomenclature_lvl1_sde , prd_item_unique_code , prd_sku_sde , BRAND_SECONDARY