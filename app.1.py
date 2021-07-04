import pandas as pd

bl = pd.read_csv( "report_blading_details-a.csv" )

clr = pd.read_csv( "report_clearance_details-a.csv" )
#clr[ 'id' ] = range( len( clr ) )
clr_pivoted = clr.pivot_table( index='service_order_id', columns='milestone_description', values='milestone_date', aggfunc='max' )
clr_so = clr[ [ 'bl_number', 'service_order_id', 'service_order_type', 'clearance_vendor_name', 'requested_date', 'defect_count', 'defect_code' ] ]
#clr_so = clr_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id', 'service_order_type', 'vendor_name', 'requested_date', 'defect_count', 'defect_code' ] )
clr_so = clr_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id' ] )

clr_merged = pd.merge( clr_so, clr_pivoted, how='left', on='service_order_id' )

trk = pd.read_csv( "report_trucking_details-a.csv" )
#clr[ 'id' ] = range( len( clr ) )
trk_pivoted = trk.pivot_table( index=[ 'service_order_id', 'container_no' ], columns='milestone_description', values='milestone_date', aggfunc='max' )
trk_so = trk[ [ 'bl_number', 'service_order_id', 'service_order_type', 'container_no', 'container_type', 'trucking_vendor_name', 'from_location', 'to_location', 'requested_date', 'defect_count', 'defect_code' ] ]
#trk_so = trk_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id', 'service_order_type', 'container_no', 'container_type', 'vendor_name', 'from_location', 'to_location', 'requested_date', 'defect_count', 'defect_code' ] )
trk_so = trk_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id', 'container_no' ] )

trk_merged = pd.merge( trk_so, trk_pivoted, how='left', on='service_order_id' )

bl1 = pd.merge( bl, clr_merged, how='left', on='bl_number' )

bl2 = pd.merge( bl1, trk_merged, how='left', on='bl_number' )


# milestone = df[ [ 'id', 'service_order_id', 'container_no', 'milestone_id', 'milestone_description', 'milestone_date' ] ]

# 'bl_number',
# 'service_order_id',
# 'service_order_type',
# 'vendor_name',
# 'requested_date',
# 'defect_count',
# 'defect_code',
# 'milestone_id',
# 'milestone_description',
# 'milestone_date',
# 'notes',
# 'sort_order'


# 'cargo_type',
# 'account_manager',
# 'job_order_date', 
# 'bl_number',
# 'customer_name',
# 'consignee_name',
# 'scope_of_work',
# 'service_type',
# 'carrier',
# 'container_count',
# 'container_no',
# 'container_type',
# 'commodity',
# 'shipment_location',
# 'shipment_date',
# 'vessel_code',
# 'terminal',
# 'overseas_port',
# 'supporting_docdate'
# 'gcss_updatedate',
# 'kewill_jobno',
# 'kewill_invoiceno',
# 'cro_date',
# 'service_order_id',
# 'service_order_type',
# 'vendor_name',
# 'from_location',
# 'to_location',
# 'requested_date',
# 'defect_count',
# 'defect_code'

clr_short = clr.drop( [ 'bl_number', 'service_order_type', 'vendor_name', 'requested_date', 'defect_count', 'defect_code', 'milestone_id', 'milestone_description', 'notes', 'sort_order' ], inplace=True, axis=1 )
# clr_pivoted = clr_short.pivot( index='service_order_id', columns='milestone_description', values='milestone_date' )  
clr_pivoted = clr_short.pivot( index='service_order_id', values='milestone_date' )  

clr_pivoted