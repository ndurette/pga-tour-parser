def compute_point(tournament, player):
    for entry in tournament.leaderboard.leader_board:
        if player.player_id == entry.player_id:
            if not entry.position:
                continue
            elif entry.position[0] == 'T':
                return tournament.points.get(entry.position[1:], 0)
            else:
                return tournament.points.get(entry.position, 0)

    return 0


def compute_points(tournaments, player):
    for t in tournaments:
        player.add_point(compute_point(t, player), t)
