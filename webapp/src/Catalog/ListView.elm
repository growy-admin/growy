module Catalog.ListView exposing (cultivarListView)

import Domain exposing (..)
import Domain.Cultivar exposing (..)
import Html exposing (Html, div, img, text, hr, i)
import Html.Attributes exposing (src, style, class)
import Maybe
import ViewHelpers exposing (..)
import Phrases exposing (..)
import Catalog.ListItemView exposing (..)
import RemoteData exposing (WebData)
import Material.Spinner as Loading exposing (..)


cultivarListView : Model -> Html Msg
cultivarListView model =
    maybeList model


centerDiv : List (Html Msg) -> Html Msg
centerDiv content =
    div
        [ style
            [ ( "display", "flex" )
            , ( "flex-direction", "row" )
            , ( "flex-grow", "1" )
            , ( "justify-content", "center" )
            ]
        ]
        [ div
            [ style
                [ ( "display", "flex" )
                , ( "flex-direction", "column" )
                , ( "justify-content", "center" )
                , ( "align-items", "center" )
                ]
            ]
            content
        ]


maybeList : Model -> Html Msg
maybeList model =
    case model.cultivars of
        RemoteData.NotAsked ->
            emptyNode

        RemoteData.Loading ->
            centerDiv
                [ Loading.spinner
                    [ Loading.active True
                    , Loading.singleColor True
                    ]
                , div
                    [ style
                        [ ( "margin-top", "6px" ) ]
                    ]
                    [ Phrases.LoadingPlants |> (tr model) |> text ]
                ]

        RemoteData.Success cultivars ->
            -- DEBUG --
            -- Just pick some smaller number until we have a proper
            -- solution to the overwhelming ammount of data
            div [ class "catalog-box-outer" ]
                [ div [ class "catalog-box-inner" ]
                    (cultivars
                        |> (cultivarListItemsView model)
                        |> (List.take 100)
                    )
                ]

        RemoteData.Failure error ->
            centerDiv [error |> toString |> Phrases.BackendError |> (tr model) |> text]


cultivarListItemsView : Model -> List Cultivar -> List (Html Msg)
cultivarListItemsView model cultivars =
    let
        selectedType =
            case model.selectedCultivar of
                Just sel ->
                    toString sel.plantType

                Nothing ->
                    ""

        filteredCultivars =
            if model.pinnedSelectedCultivar == Just True then
                List.filter
                    (\a -> (toString a.plantType) == selectedType)
                    cultivars
            else
                cultivars

        groupedByType =
            groupCultivarsOnType filteredCultivars

        processCultivarGroup =
            \cultivarGroup ->
                (List.map (cultivarListItemView model) <| cultivarGroup)
    in
        List.concat (List.map processCultivarGroup groupedByType)
