import pandas as pd

bl = pd.read_csv( "report_bl_details.1.csv" )
clr = pd.read_csv( "report_clr_details.1.csv" )
trk = pd.read_csv( "report_trk_details.1.csv" )

clr_pivoted = clr.pivot_table( index='service_order_id', columns='milestone_description', values='milestone_date', aggfunc='max' )
clr_so = clr[ [ 'bl_number', 'service_order_id', 'service_order_type', 'clearance_vendor_name', 'requested_date', 'defect_count', 'defect_code' ] ]
clr_so = clr_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id' ] )
clr_merged = pd.merge( clr_so, clr_pivoted, how='left', on='service_order_id' )


trk_pivoted = trk.pivot_table( index=[ 'service_order_id', 'container_no' ], columns='milestone_description', values='milestone_date', aggfunc='max' )
trk_so = trk[ [ 'bl_number', 'service_order_id', 'service_order_type', 'container_no', 'container_type', 'trucking_vendor_name', 'from_location', 'to_location', 'requested_date', 'defect_count', 'defect_code' ] ]
trk_so = trk_so.drop_duplicates( subset=[ 'bl_number', 'service_order_id', 'container_no' ] )
trk_merged = pd.merge( trk_so, trk_pivoted, how='left', on=[ 'service_order_id', 'container_no' ] )

# bl1 = pd.merge( bl, clr_merged, how='left', on='bl_number' )
# bl2 = pd.merge( bl1, trk_merged, how='left', on='bl_number' )

so_merged = clr_merged.append( [ trk_merged ] )
final = pd.merge( bl, so_merged, how='left', on='bl_number' )
final.to_excel( 'bl_tracking_report.xlsx' )


